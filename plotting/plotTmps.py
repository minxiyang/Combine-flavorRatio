import ROOT
import numpy as np
from func.average import average
from func.getAccEffAndErr import getAccEffAndErr
import numpy as np

def plotTmps(year, cg, massCut, tmps, fr=1.):

    ROOT.gStyle.SetOptStat(0)
    
    for flavor in ["mu", "el"]:
        
        
        dy_sig=tmps[flavor+'_DY_S'].Clone()
        dy_sig.Scale(fr)
        dy_bkg=tmps[flavor+'_DY_B'].Clone()
        otherHist=tmps[flavor+'_Other'].Clone()
        dataHist=tmps[flavor+'_data_obs'].Clone()
        acceffs=getAccEffAndErr(year, cg, massCut)
        acceff=acceffs[0]
        average(dataHist)
        average(otherHist)
        average(dy_sig)
        average(dy_bkg)
        if flavor == "mu": dy_sig.Scale(acceff)
        ly=ROOT.TLegend(0.55,0.7,0.9,0.9)
        otherHist.SetFillColor(ROOT.kYellow)
        dy_bkg.SetFillColor(ROOT.kGreen)
        dy_sig.SetFillColor(ROOT.kRed)
        ly.AddEntry(otherHist, "Other")
        ly.AddEntry(dy_sig, "DY above the masscut")
        ly.AddEntry(dy_bkg, "DY below the masscut")
        ly.AddEntry(dataHist, "Data")
        Stack=ROOT.THStack("stack","")
        Stack.Add(otherHist)
        Stack.Add(dy_bkg)
        Stack.Add(dy_sig)
        c=ROOT.TCanvas("c","c",800,800)
        plotPad = ROOT.TPad("plotPad","plotPad",0,0.25,1,1)
        ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0,1,0.25)
        plotPad.Draw()
        ratioPad.Draw()
        plotPad.cd()
        plotPad.SetLogy()
        plotPad.SetLogx()
        Stack.Draw("hist")
        Stack.GetYaxis().SetTitle('Event/GeV')
        Stack.GetXaxis().SetLabelSize(0.0)
        Stack.GetXaxis().SetMoreLogLabels()
        Stack.SetMinimum(1e-3)
        Stack.SetMaximum(3e2)
        if flavor == "el": Stack.SetTitle("dielectron"+" "+year+" "+cg)
        else: Stack.SetTitle("dimuon"+" "+year+" "+cg)
        dataHist.SetMarkerStyle(8)
        dataHist.SetLineColor(1)
        dataHist.Draw("samep")
        ly.Draw()
        ratioPad.cd()
        ratioPad.SetLogx()
        ratioPad.SetTopMargin(0.05)
        ratioPad.SetBottomMargin(0.25)
        ratioHist=dataHist.Clone()
        ratioHist.SetTitle(" ")
        ratioHist.GetYaxis().SetRangeUser(0, 2)
        ratioHist.GetYaxis().SetTitle("Data/MC")
        ratioHist.GetYaxis().SetLabelSize(0.08)
        ratioHist.GetXaxis().SetLabelSize(0.08)
        ratioHist.GetXaxis().SetTitle('Reco Mass [GeV]')
        ratioHist.GetXaxis().SetMoreLogLabels()
        ratioHist.GetXaxis().SetTitleSize(0.08)
        ratioHist.GetYaxis().SetTitleSize(0.08)
        ratioHist.GetYaxis().SetTitleOffset(0.4)
        ratioHist.GetXaxis().SetTitleOffset(1.1)
        ratioHist.GetYaxis().SetNdivisions(502)
        tempHist=dy_sig.Clone()
        tempHist.Add(dy_bkg)
        tempHist.Add(otherHist)

        for i in range(0,ratioHist.GetNbinsX()+1):

            dataVal=dataHist.GetBinContent(i)
            dataErr=dataHist.GetBinError(i)
            mcVal=tempHist.GetBinContent(i)
            mcErr=tempHist.GetBinError(i)
            val=dataVal/mcVal
            err=val*np.sqrt((dataErr/dataVal)**2+(mcErr/mcVal)**2)
            ratioHist.SetBinContent(i, val)
            ratioHist.SetBinError(i, err)
        
        ratioHist.Draw("p")
        treLine = ROOT.TLine(300, 1.0, 3500, 1.0)
        treLine.SetLineStyle(2)
        treLine.Draw()
        c.Update()
        if fr==1: plotName = flavor+"_"+year+"_"+cg+"_cut"+str(massCut)+"_template.pdf"
        else: plotName = flavor+"_"+year+"_"+cg+"_cut"+str(massCut)+"_"+str(fr)+"fr"+"_template.pdf"
        c.Print("plots/templates/"+plotName)


