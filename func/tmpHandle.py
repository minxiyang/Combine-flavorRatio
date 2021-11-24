import ROOT
from Parameters import data_files, shape_corr, def_bng
from func.getBngs import getBngs
from func.Rebin import Rebin
import numpy as np


class tmpHandle(object):

    def __init__(self, year, cg, scale="Run2"):

         self.year=year
         self.cg=cg
         self.scale=scale

    def createTmps(self, massCut, sys_uncers, istoy=False, fr=1., chan="mu", isSingleBin=False, massCutH=0, isFold=False, isMultiBin=False):

        print("create templates for %s %s"%(self.year, self.cg) )
        templates={}
        bins=def_bng
        print(bins) 
        for flavor in ['mu', 'el']:
             
            bng=getBngs(flavor, self.year, self.cg, 150)
            #bng=np.append(bng[:-1],[2000,2500,3000,3500])
            if isMultiBin:
                #bins=[200,300,400,500,690,900,1250,1610,2000,3500]
                bng=np.asarray(bins,dtype=np.float64)
            #print(bng)
            if isFold: 
                if massCutH<3500:bins=[1, massCut, massCutH, 3500]
                else: bins=[1, massCut, 3500]
                bng=np.asarray(bins,dtype=np.float64)
                #bng=np.append(bng,[,2000, 3500])
                massCut1=massCut
                massCutH1=massCutH
                massCut=150
                massCutH=3500
            dy_file='DY_'+flavor+'_'+self.year+'.root'
            if flavor=='el':histName_dy='DielectronResponse_'+self.cg
            else: histName_dy="DimuonResponse_"+self.cg

            f_dy=ROOT.TFile.Open("MC/"+dy_file,"r")
            dyHist2D=f_dy.Get(histName_dy)
            dyHist2D.SetDirectory(0)
            dyHist2Dvar={}

            uncers=sys_uncers[flavor]

            for uncer in uncers:
               
                dyHist2Dvar[uncer]=f_dy.Get(histName_dy+'_'+uncer)
                dyHist2Dvar[uncer].SetDirectory(0)

            f_dy.Close()

            other_file='Other_'+flavor+'_'+self.year+'.root'

            if flavor=="el":histName_other='DielectronMass_'+self.cg
            else: histName_other="DimuonMassVertexConstrained_"+self.cg

            f_other=ROOT.TFile.Open("MC/"+other_file,"r")
            otherHist=f_other.Get(histName_other)
            otherHist.SetDirectory(0)
            otherHistvar={}

            for uncer in uncers:
                otherHistvar[uncer]=f_other.Get(histName_other+'_'+uncer)
                otherHistvar[uncer].SetDirectory(0)

            f_other.Close()
            templates[flavor+'_Other']=Rebin(otherHist, flavor+'_Other', flavor, self.cg, bng, scale=self.scale)
            #templates[flavor+'_Other']=otherHist.Rebin(len(bng)-1, flavor+'_Other', bng)

            for key in otherHistvar.keys():
 
                
                if "MassScale" in key: key=flavor+key
                
                for corr in shape_corr:
                    key1=key.strip('Up')
                    key2=key1.strip('Down')
                    if key2 in corr and self.cg in corr and self.year in corr: key=corr.split("_")[0]+"_"+key
                if 'Up' in key or 'Down' in key:
                    templates[flavor+'_Other_'+key]=Rebin(otherHist, flavor+'_Other_'+key, flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_Other_'+key]=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key, bng)
                else:
                    templates[flavor+'_Other_'+key+'Up']=Rebin(otherHist, flavor+'_Other_'+key+'Up', flavor, self.cg, bng, scale=self.scale)
                    templates[flavor+'_Other_'+key+'Down']=Rebin(otherHist, flavor+"_Other_"+key+'Down', flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_Other_'+key+'Up']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key+'Up', bng)
                    #templates[flavor+'_Other_'+key+'Down']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key+'Down', bng)
                
            nBins=int(massCut/10.)
            if isSingleBin:
                nBinsL=nBins
                nBinsH=int(massCutH/10.)
                if nBinsH>=350 or nBinsH<=nBinsL: 
                    isSingleBin=False
                else:
                    dy_sig=dyHist2D.ProjectionX("sigx", nBinsL+1, nBinsH)
                    templates[flavor+'_DY_S']=Rebin(dy_sig, flavor+'_DY_S', flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_DY_S']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S', bng)
                    dy_bkgL=dyHist2D.ProjectionX("bkgxl", 15, nBinsL)
                    templates[flavor+'_DY_BL']=Rebin(dy_bkgL, flavor+'_DY_BL', flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_DY_BL']=dy_bkgL.Rebin(len(bng)-1, flavor+'_DY_BL', bng)
                    dy_bkgH=dyHist2D.ProjectionX("bkgxh", nBinsH+1, -1)
                    templates[flavor+'_DY_BH']=Rebin(dy_bkgH, flavor+'_DY_BH', flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_DY_BH']=dy_bkgH.Rebin(len(bng)-1, flavor+'_DY_BH', bng)

                    for key in dyHist2Dvar.keys():

                        keynew=key
                        if "MassScale" in key: keynew=flavor+key
                        for corr in shape_corr:
                            key1=keynew.strip('Up')
                            key2=key1.strip('Down')

                            if key2 in corr and self.cg in corr and self.year in corr: keynew=corr.split("_")[0]+"_"+keynew

                        if 'Up' in key or 'Down' in key:

                            dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBinsL+1, nBinsH)
                            templates[flavor+'_DY_S_'+keynew]=Rebin(dy_sig, flavor+'_DY_S_'+keynew, flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_S_'+keynew]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew, bng)
                            dy_bkgL=dyHist2D.ProjectionX("bkgxl", 15, nBinsL)
                            templates[flavor+'_DY_BL_'+keynew]=Rebin(dy_bkgL, flavor+'_DY_BL_'+keynew, flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_BL_'+keynew]=dy_bkgL.Rebin(len(bng)-1, flavor+'_DY_BL_'+keynew, bng)
                            dy_bkgH=dyHist2D.ProjectionX("bkgxh", nBinsH+1, -1)
                            #templates[flavor+'_DY_BH_'+keynew]=dy_bkgH.Rebin(len(bng)-1, flavor+'_DY_BH_'+keynew, bng)
                            templates[flavor+'_DY_BH_'+keynew]=Rebin(dy_bkgH, flavor+'_DY_BH_'+keynew, flavor, self.cg, bng, scale=self.scale)

                        else:

                            dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBinsL+1, nBinsH)
                            templates[flavor+'_DY_S_'+keynew+'Up']=Rebin(dy_sig, flavor+'_DY_S_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                            templates[flavor+'_DY_S_'+keynew+'Down']=Rebin(dy_sig, flavor+'_DY_S_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_S_'+keynew+'Up']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Up', bng)
                            #templates[flavor+'_DY_S_'+keynew+'Down']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Down', bng)
                            dy_bkgL=dyHist2D.ProjectionX("bkgx", 15, nBinsL)
                            templates[flavor+'_DY_BL_'+keynew+'Up']=Rebin(dy_bkgL, flavor+'_DY_BL_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                            templates[flavor+'_DY_BL_'+keynew+'Down']=Rebin(dy_bkgL, flavor+'_DY_BL_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_BL_'+keynew+'Up']=dy_bkgL.Rebin(len(bng)-1, flavor+'_DY_BL_'+keynew+'Up', bng)
                            #templates[flavor+'_DY_BL_'+keynew+'Down']=dy_bkgL.Rebin(len(bng)-1, flavor+'_DY_BL_'+keynew+'Down', bng)
                            dy_bkgH=dyHist2D.ProjectionX("bkgx", nBinsH+1, -1)
                            templates[flavor+'_DY_BH_'+keynew+'Up']=Rebin(dy_bkgH, flavor+'_DY_BH_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                            templates[flavor+'_DY_BH_'+keynew+'Down']=Rebin(dy_bkgH, flavor+'_DY_BH_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_BH_'+keynew+'Up']=dy_bkgH.Rebin(len(bng)-1, flavor+'_DY_BH_'+keynew+'Up', bng)
                            #templates[flavor+'_DY_BH_'+keynew+'Down']=dy_bkgH.Rebin(len(bng)-1, flavor+'_DY_BH_'+keynew+'Down', bng)
                    
            elif isMultiBin:
                genBng=[0]+massCutH[:-1]+[-10]
                #print(genBng)
                for i in range(len(genBng)-1):
                    nBinsH=int(genBng[i+1]/10.)
                    nBinsL=int(genBng[i]/10.)

                    dy_sig=dyHist2D.ProjectionX("sigx"+str(i), nBinsL+1, nBinsH)
                    templates[flavor+'_DY_S'+str(i)]=Rebin(dy_sig, flavor+'_DY_S'+str(i), flavor, self.cg, bng, scale=self.scale)
                    #templates[flavor+'_DY_S'+str(i)]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S'+str(i), bng)

                    for key in dyHist2Dvar.keys():

                        keynew=key
                        if "MassScale" in key: keynew=flavor+key
                        for corr in shape_corr:
                            key1=keynew.strip('Up')
                            key2=key1.strip('Down')

                            if key2 in corr and self.cg in corr and self.year in corr: keynew=corr.split("_")[0]+"_"+keynew

                        if 'Up' in key or 'Down' in key:

                            dy_sig=dyHist2Dvar[key].ProjectionX("sigx"+str(i), nBinsL+1, nBinsH)
                            templates[flavor+'_DY_S'+str(i)+'_'+keynew]=Rebin(dy_sig, flavor+'_DY_S'+str(i)+'_'+keynew, flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_S'+str(i)+'_'+keynew]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S'+str(i)+'_'+keynew, bng)
                        else:
                            dy_sig=dyHist2Dvar[key].ProjectionX("sigx"+str(i), nBinsL+1, nBinsH)
                            templates[flavor+'_DY_S'+str(i)+'_'+keynew+'Up']=Rebin(dy_sig, flavor+'_DY_S'+str(i)+'_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                            templates[flavor+'_DY_S'+str(i)+'_'+keynew+'Down']=Rebin(dy_sig, flavor+'_DY_S'+str(i)+'_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                            #templates[flavor+'_DY_S'+str(i)+'_'+keynew+'Up']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S'+str(i)+'_'+keynew+'Up', bng)
                            #templates[flavor+'_DY_S'+str(i)+'_'+keynew+'Down']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S'+str(i)+'_'+keynew+'Down', bng)


            else:
                dy_sig=dyHist2D.ProjectionX("sigx", nBins+1, -1)
                templates[flavor+'_DY_S']=Rebin(dy_sig, flavor+'_DY_S', flavor, self.cg, bng, scale=self.scale)
                #templates[flavor+'_DY_S']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S', bng)
                dy_bkg=dyHist2D.ProjectionX("bkgx", 15, nBins)
                #templates[flavor+'_DY_B']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B', bng)
                templates[flavor+'_DY_B']=Rebin(dy_bkg, flavor+'_DY_B', flavor, self.cg, bng, scale=self.scale)


                for key in dyHist2Dvar.keys():
            
                    keynew=key
                    if "MassScale" in key: keynew=flavor+key
                    for corr in shape_corr:
                        key1=keynew.strip('Up')
                        key2=key1.strip('Down')
                  
                        if key2 in corr and self.cg in corr and self.year in corr: keynew=corr.split("_")[0]+"_"+keynew

                    if 'Up' in key or 'Down' in key:
             
                        dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                        templates[flavor+'_DY_S_'+keynew]=Rebin(dy_sig, flavor+'_DY_S_'+keynew, flavor, self.cg, bng, scale=self.scale)
                        #templates[flavor+'_DY_S_'+keynew]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew, bng)
                        dy_bkg=dyHist2D.ProjectionX("bkgx", 15, nBins)
                        templates[flavor+'_DY_B_'+keynew]=Rebin(dy_bkg, flavor+'_DY_B_'+keynew, flavor, self.cg, bng, scale=self.scale)
                        #templates[flavor+'_DY_B_'+keynew]=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew, bng)

                    else:
 
                        dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                        templates[flavor+'_DY_S_'+keynew+'Up']=Rebin(dy_sig, flavor+'_DY_S_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                        templates[flavor+'_DY_S_'+keynew+'Down']=Rebin(dy_sig, flavor+'_DY_S_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                        #templates[flavor+'_DY_S_'+keynew+'Up']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Up', bng)
                        #templates[flavor+'_DY_S_'+keynew+'Down']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Down', bng)
                        dy_bkg=dyHist2D.ProjectionX("bkgx", 15, nBins)
                        templates[flavor+'_DY_B_'+keynew+'Up']=Rebin(dy_bkg, flavor+'_DY_B_'+keynew+'Up', flavor, self.cg, bng, scale=self.scale)
                        templates[flavor+'_DY_B_'+keynew+'Down']=Rebin(dy_bkg, flavor+'_DY_B_'+keynew+'Down', flavor, self.cg, bng, scale=self.scale)
                        #templates[flavor+'_DY_B_'+keynew+'Up']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew+'Up', bng)
                        #templates[flavor+'_DY_B_'+keynew+'Down']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew+'Down', bng)

            if not istoy and self.scale=="Run2":

                files=data_files

                if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
                else: files = [file_ for file_ in files if 'ele' in file_]

                if self.year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
                elif self.year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
                else:                 files=[file_ for file_ in files if '_2018' in file_]

                if self.cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
                else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

                datafile=files[0]
                data=[]
                f=open("dataList/"+datafile,"r")
                for m in f:

                    m=float(m)
                    data.append(m)
                f.close()
                dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)
                for mass in data: dataHist.Fill(mass)

            elif istoy:

                dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)
                if flavor+'_DY_BL' in templates.keys():
                    dataHist.Add(templates[flavor+'_DY_BL'])
                    dataHist.Add(templates[flavor+'_DY_BH'])
                else:
                    dataHist.Add(templates[flavor+'_DY_B'])
                dataHist.Add(templates[flavor+'_Other'])
                if flavor==chan: dataHist.Add(templates[flavor+'_DY_S'], fr)
                else: dataHist.Add(templates[flavor+'_DY_S'])

            else:
                tempHist=ROOT.TH1D(flavor+'_tmp', flavor+'_tmp', len(bng)-1,bng)
                tempHist.Add(templates[flavor+'_DY_S'])
                tempHist.Add(templates[flavor+'_DY_B'])
                tempHist.Add(templates[flavor+'_Other'])
                dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)
                for i in range(tempHist.GetNbinsX()+1):
                  
                    mean=tempHist.GetBinContent(i)
                    #if i == 0: 
                    #    dataHist.SetBinContent(i, mean)
                    #else:
                    val=np.random.poisson(mean, 1)
                    #print (val)
                    dataHist.SetBinContent(i, val[0])

            templates[flavor+'_data_obs']=dataHist.Clone()
            if isFold:
                for key in templates.keys():
                    if flavor not in key: continue
                    for i in range(len(bng+1)):
                        if i!= 2: 
                            templates[key].SetBinContent(i,0)
                            templates[key].SetBinError(i,0)
                    if "DY_B" in key: 
                        templates.pop(key)
                    else:
                        name=templates[key].GetName()                     
                        tempHist=ROOT.TH1D("temp", "", 1, templates[key].GetBinLowEdge(2), templates[key].GetBinLowEdge(3))
                        tempHist.SetBinContent(1, templates[key].GetBinContent(2))
                        templates.pop(key)
                        tempHist.SetName(name)
                        templates[key]=tempHist.Clone()
                        templates[key].SetBinContent(0,0)
                        templates[key].SetBinContent(-1,0)
                massCut=massCut1
                massCutH=massCutH1
        self.templates=templates

    def saveTmps(self, tmpName):

        print('save templates for %s %s'%(self.year, self.cg))
        if "mu_DY_S0" in self.templates.keys():
            nev_el_dy_s=[]
            nev_mu_dy_s=[]
            for i in range(1,10):
                nev_el_dy_s.append(self.templates['el_DY_S'+str(i)].Integral())
                nev_mu_dy_s.append(self.templates['mu_DY_S'+str(i)].Integral())
                self.templates['el_DY_S'+str(i)].Scale(1.0/nev_el_dy_s[i-1])
                self.templates['mu_DY_S'+str(i)].Scale(1.0/nev_mu_dy_s[i-1])
                for key in self.templates.keys():
                    if 'el_DY_S'+str(i)+'_' in key: self.templates[key].Scale(1.0/nev_el_dy_s[i-1])
                    elif 'mu_DY_S'+str(i)+'_' in key: self.templates[key].Scale(1.0/nev_mu_dy_s[i-1])
            
            tempFiles=ROOT.TFile.Open("templates/"+tmpName+".root","RECREATE")
            for key in self.templates.keys():self.templates[key].Write()
            tempFiles.Save()
            tempFiles.Close()
            for i in range(1,10):
                self.templates['el_DY_S'+str(i)].Scale(nev_el_dy_s[i-1])
                self.templates['mu_DY_S'+str(i)].Scale(nev_mu_dy_s[i-1])
                for key in self.templates.keys():
                    if 'el_DY_S'+str(i)+'_' in key: self.templates[key].Scale(nev_el_dy_s[i-1])
                    elif 'mu_DY_S'+str(i)+'_' in key: self.templates[key].Scale(nev_mu_dy_s[i-1])

        else:
            nev_el_dy_s=self.templates['el_DY_S'].Integral()
            nev_mu_dy_s=self.templates['mu_DY_S'].Integral()
            for key in self.templates.keys():
                if 'mu_DY_S' in key: self.templates[key].Scale(1.0/nev_mu_dy_s)
                elif 'el_DY_S' in key: self.templates[key].Scale(1.0/nev_el_dy_s)

            tempFiles=ROOT.TFile.Open("templates/"+tmpName+".root","RECREATE")
            for key in self.templates.keys(): self.templates[key].Write()
            tempFiles.Save()
            tempFiles.Close()
            for key in self.templates.keys():
                if 'mu_DY_S' in key: self.templates[key].Scale(nev_mu_dy_s)
                elif 'el_DY_S' in key: self.templates[key].Scale(nev_el_dy_s)

    

    def loadTmps(self, tmpName, sys_uncers, isSingleBin=False):

        print('load templates '+tmpName)
        
        templates={}
        tmpFile=ROOT.TFile.Open("templates/"+tmpName+".root","r")
        if isSingleBin: processes=["DY_S", "DY_BH", "DY_BL", "Other"]
        else: processes=["DY_S", "DY_B", "Other"]
        for flavor in ["mu", "el"]:
            templates[flavor+"_data_obs"]=tmpFile.Get(flavor+"_data_obs")
            templates[flavor+"_data_obs"].SetDirectory(0)
            for process in processes:
                templates[flavor+"_"+process]=tmpFile.Get(flavor+"_"+process)
                templates[flavor+"_"+process].SetDirectory(0)
                for uncer in sys_uncers[flavor]:
                    if "Up" in uncer or "Down" in uncer: templates[flavor+"_"+process+"_"+uncer]=tmpFile.Get(flavor+"_"+process+"_"+flavor+uncer)
                    else: templates[flavor+"_"+process+"_"+uncer]=tmpFile.Get(flavor+"_"+process+"_"+flavor+uncer+"Up") 
                    templates[flavor+"_"+process+"_"+uncer].SetDirectory(0)

        self.templates=templates
