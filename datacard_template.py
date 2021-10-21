import ROOT
import math
import numpy as np
from Variables import data_files, sys_uncers_el, sys_uncers_mu



def getBngs(flavor, year, cg, masscut):
    
    files=data_files

    if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
    else: files = [file_ for file_ in files if 'ele' in file_]
    
    if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
    elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
    else:                 files=[file_ for file_ in files if '_2018' in file_]
    
    if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
    else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]
    
    datafile=files[0]
    eventList=[]
    f=open("Data/"+datafile,"r")
    for m in f:

        m=float(m)
        eventList.append(m)

    f.close()
    eventList.sort()
    miniSize=10
    miniN=20
    bins=[]
    bins.append(3500)
    ith=0
    delta_ith=0
    eventList.reverse()
    for i in range(len(eventList)):
        delta_ith+=1
        if (eventList[ith]-eventList[i])>miniSize and delta_ith>miniN and eventList[i]>masscut:
            binEdge=math.ceil(eventList[i])
            bins.append(binEdge)
            ith=i
            delta_ith=0
        elif eventList[i]<masscut:
            bins[-1]=masscut
            break
    bins.reverse()
    bng=np.asarray(bins,dtype=np.float64)
    return bng



def tempAndCard(year, cg, massCut):
        
    templates={}
    for flavor in ['mu', 'el']:

        bng=getBngs(flavor, year, cg, 400)
        dy_file='DY_'+flavor+'_'+year+'.root'
        if flavor=='el':histName_dy='DielectronResponse_'+cg
        else: histName_dy="DimuonResponse_"+cg
        
        f_dy=ROOT.TFile.Open("dataCollection/"+dy_file,"r")
        dyHist2D=f_dy.Get(histName_dy)
        dyHist2D.SetDirectory(0)
        dyHist2Dvar={}
        if flavor=='el':uncerts=sys_uncers_el
        else:uncerts=sys_uncers_mu

        for uncert in uncerts:
            dyHist2Dvar[uncert]=f_dy.Get(histName_dy+'_'+uncert)
            dyHist2Dvar[uncert].SetDirectory(0)
        f_dy.Close()

        other_file='Other_'+flavor+'_'+year+'.root'
        if flavor=="el":histName_other='DielectronMass_'+cg
        else: histName_other="DimuonMassVertexConstrained_"+cg
        f_other=ROOT.TFile.Open("dataCollection/"+other_file,"r")
        otherHist=f_other.Get(histName_other)
        otherHist.SetDirectory(0)
        otherHistvar={}
        for uncert in uncerts:
            otherHistvar[uncert]=f_other.Get(histName_other+'_'+uncert)
            otherHistvar[uncert].SetDirectory(0)
        f_other.Close()
        
        templates[flavor+'_Other']=otherHist.Rebin(len(bng)-1, flavor+'_Other', bng)
        for key in otherHistvar.keys():
            if 'Up' in key or 'Down' in key:
                templates[flavor+'_Other_'+key]=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+flavor+key, bng)
            else:
                templates[flavor+'_Other_'+key+'Up']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+flavor+key+'Up', bng)
                templates[flavor+'_Other_'+key+'Down']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+flavor+key+'Down', bng)

        nBins=int(massCut/10.)
        dy_sig=dyHist2D.ProjectionX("sigx", nBins+1, -1)
        templates[flavor+'_DY_S']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S', bng)
        dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
        templates[flavor+'_DY_B']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B', bng)

        for key in dyHist2Dvar.keys():

            if 'Up' in key or 'Down' in key:
                dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                templates[flavor+'_DY_S_'+key]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+flavor+key, bng)
                dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
                templates[flavor+'_DY_B_'+key]=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+flavor+key, bng)
            else:
                dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                templates[flavor+'_DY_S_'+key+'Up']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+flavor+key+'Up', bng)
                templates[flavor+'_DY_S_'+key+'Down']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+flavor+key+'Down', bng)
                dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
                templates[flavor+'_DY_B_'+key+'Up']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+flavor+key+'Up', bng)
                templates[flavor+'_DY_B_'+key+'Down']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+flavor+key+'Down', bng)
        
        files=data_files

        if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
        else: files = [file_ for file_ in files if 'ele' in file_]

        if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
        elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
        else:                 files=[file_ for file_ in files if '_2018' in file_]

        if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
        else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

        datafile=files[0]
        data=[]
        f=open("Data/"+datafile,"r")
        for m in f:

            m=float(m)
            data.append(m)
        f.close()
        dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)    
        for mass in data: dataHist.Fill(mass)
        templates[flavor+'_data_obs']=dataHist.Clone()

    tmpName=year+"_"+cg+".root"

    print('write datacards')

    tmpcard=open("datacards/tmp/card_tmp.txt", "r") 
    tmptxt=tmpcard.read()
    tmptxt=tmptxt.replace('tmp.root',tmpName)
    nev_mu_obs=templates['mu_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_mu_obs',str(nev_mu_obs))
    nev_el_obs=templates['el_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_el_obs',str(nev_el_obs))
    nev_el_dy_s=templates['el_DY_S'].Integral()
    tmptxt=tmptxt.replace('nev_el_dy_s',str(nev_el_dy_s))
    nev_mu_dy_s=templates['mu_DY_S'].Integral()
    tmptxt=tmptxt.replace('nev_mu_dy_s',str(nev_mu_dy_s))
    nev_el_dy_b=templates['el_DY_B'].Integral()
    tmptxt=tmptxt.replace('nev_el_dy_b',str(nev_el_dy_b))
    nev_mu_dy_b=templates['mu_DY_B'].Integral()
    tmptxt=tmptxt.replace('nev_mu_dy_b',str(nev_mu_dy_b))
    nev_el_o=templates['el_Other'].Integral()
    tmptxt=tmptxt.replace('nev_el_o',str(nev_el_o))
    nev_mu_o=templates['mu_Other'].Integral()
    tmptxt=tmptxt.replace('nev_mu_o',str(nev_mu_o))
    acc_eff_med=nev_mu_dy_s/nev_el_dy_s 
    acc_eff_low=acc_eff_med-0.0001
    acc_eff_high=acc_eff_med+0.0001
    tmptxt=tmptxt.replace('acc_eff_med',str(acc_eff_med))
    tmptxt=tmptxt.replace('acc_eff_low',str(acc_eff_low))
    tmptxt=tmptxt.replace('acc_eff_high',str(acc_eff_high))
    datacard=open("datacards/"+year+"_"+cg+".txt", "w")  
    datacard.write(tmptxt)
    tmpcard.close()
    datacard.close()
    
    print('save templates')
    for key in templates.keys():
        if 'mu_DY_S' in key: templates[key].Scale(nev_el_dy_s/nev_mu_dy_s)
    tempFiles=ROOT.TFile.Open("templates/"+tmpName,"RECREATE")
    for key in templates.keys(): templates[key].Write()
    tempFiles.Save()
    tempFiles.Close()


for year in ['2016','2017','2018']:
    for cg in ['bb','be']:

        tempAndCard(year, cg, 800)

