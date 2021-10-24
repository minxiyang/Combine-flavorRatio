import ROOT
import math
import numpy as np

ROOT.gStyle.SetOptStat(0)
data_files=["dimuon_Mordion2017_BB.txt",  "eventList_ele_2016_BB.txt",  "eventList_ele_2017_BB.txt",  "eventList_ele_2018_BB.txt", "event_list_2017_bb_clean_sort.txt",    "event_list_2018_bb_clean_sort.txt",  "dimuon_Mordion2017_BE.txt",  "eventList_ele_2016_BE.txt",  "eventList_ele_2017_BE.txt",  "eventList_ele_2018_BE.txt",  "event_list_2017_beee_clean_sort.txt",  "event_list_2018_beee_clean_sort.txt"]
binning=[400, 411, 422, 434, 446, 459, 472, 486, 500, 515, 531, 547, 564, 582, 601, 621, 642, 664, 687, 711, 736, 762, 790, 819, 850, 882, 919, 955, 993, 1034, 1093, 1157, 1289, 1605, 3500]
#bng=np.array(binning)
bng=np.asarray(binning,dtype=np.float64)
cut=800
def average(hist):
    for i in range(0, hist.GetNbinsX()+2):
        val=hist.GetBinContent(i)
        err=hist.GetBinError(i)
        wid=hist.GetBinWidth(i)
        val=val/wid
        err=err/wid
        #if i==hist.GetNbinsX()+1:
       
        hist.SetBinContent(i,val)
        hist.SetBinError(i,err)


def plot(flavor, year, cg, massCut):


    for file_ in data_files:
        key=""
        if 'dimuon' in file_ or 'clean' in file_:
                key+='mu_'
        else:
                key+='el_'

        if 'Mordion2017' in file_ or '2016' in file_:
                key+='2016_'
        elif '_2017' in file_:
                key+='2017_'
        else:
                key+='2018_'
        if 'BB' in file_ or 'bb' in file_:
                key+='bb'
        else:
                key+='be'
        
        #data=[]
        #print(key)
        #print(flavor+'_'+year+'_'+cg+"run")
        if key == flavor+'_'+year+'_'+cg:
            data=[]
            f=open("dataList/"+file_,"r")
            for m in f:

                m=float(m)
                data.append(m)
            f.close()

    
    other_file="Other_"+flavor+"_"+year+".root"
    dy_file="DY_"+flavor+"_"+year+".root"
    Stack=ROOT.THStack("stack","")
    dataHist=ROOT.TH1D('dataHist', 'dataHist', len(bng)-1,bng)
    print(len(data))
    for mass in data:
        dataHist.Fill(mass)

    if flavor=="el":histName_other='DielectronMass_'+cg
    else: histName_other="DimuonMassVertexConstrained_"+cg
    f_other=ROOT.TFile.Open("MC/"+other_file,"r")
    otherHist=f_other.Get(histName_other)
    #otherHist.SetDirectory(0)
    otherHist=otherHist.Rebin(len(bng)-1,'other_mc' ,bng)
    otherHist.SetDirectory(0)
    otherHist.GetBinContent(1)
    f_other.Close()
    
    if flavor=="el":histName_dy='DielectronResponse_'+cg
    else: histName_dy="DimuonResponse_"+cg
    f_dy=ROOT.TFile.Open("MC/"+dy_file,"r")
    dyHist2D=f_dy.Get(histName_dy)
    dyHist2D.SetDirectory(0)
    f_dy.Close()
    nBins=int(massCut/10.)
    dy_sig=dyHist2D.ProjectionX("sigx", nBins+1, -1)
    dy_sig=dy_sig.Rebin(len(bng)-1,'dy_sig' ,bng)
    dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
    dy_bkg=dy_bkg.Rebin(len(bng)-1,'dy_bkg' ,bng)

    average(dataHist)
    average(otherHist)
    average(dy_sig)
    average(dy_bkg)
    ly=ROOT.TLegend(0.73,0.8,0.92,0.92)
    otherHist.SetFillColorAlpha(ROOT.kYellow,0.5)
    dy_bkg.SetFillColorAlpha(ROOT.kGreen,0.5)
    dy_sig.SetFillColorAlpha(ROOT.kRed,0.5)
    ly.AddEntry(otherHist, "other mc")
    ly.AddEntry(dy_sig, "DY sig")
    ly.AddEntry(dy_bkg, "DY bkg")
    ly.AddEntry(dataHist, "data")
    otherHist.GetYaxis().SetRangeUser(1e-5, 1e3)
    dy_bkg.GetYaxis().SetRangeUser(1e-5, 1e3)
    dy_sig.GetYaxis().SetRangeUser(1e-5, 1e3)
    Stack.Add(otherHist)
    Stack.Add(dy_bkg)
    Stack.Add(dy_sig)
    Stack.Draw() 
    Stack.GetYaxis().SetTitle('Event/GeV')
    Stack.GetXaxis().SetTitle('Reco Mass [GeV]')
    Stack.GetYaxis().SetRangeUser(1e-5, 1e3)
    c=ROOT.TCanvas("c","c",800,800)
    c.SetLogy()
    c.SetLogx()
    Stack.GetYaxis().SetRangeUser(1e-5, 1e3)
    Stack.Draw("hist")
    dataHist.SetMarkerStyle(8)
    otherHist.GetYaxis().SetRangeUser(1e-5, 1e3)
    
    dataHist.GetYaxis().SetRangeUser(1e-5, 1e3) 
    #dataHist.SetMarkerSize(40)
    dataHist.Draw("samep")
    ly.Draw()
    c.Update()
    Stack.GetYaxis().SetRangeUser(1e-5, 1e3)
    c.Print("plots/template/"+flavor+"_"+year+"_"+cg+"_template.pdf")
    Stack.GetYaxis().SetRangeUser(1e-5, 1e3) 

for flavor in ['mu','el']:
    for year in ['2016','2017','2018']:
        for cg in ['bb','be']:


            plot(flavor, year, cg, cut)
