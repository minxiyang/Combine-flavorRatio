import ROOT
import numpy as np
from func.average import average
import numpy as np
from plotting.setTDRStyle import setTDRStyle
from Parameters import lumi_el, lumi_mu

def plotTmps(year, cg, massCut, tmps, fr=1.):

    ROOT.gStyle.SetOptStat(0)
    
    for flavor in ["mu", "el"]:
        
        
        dy_sig=tmps[flavor+'_DY_S'].Clone()
        dy_sig.Scale(fr)
        dy_bkg=tmps[flavor+'_DY_B'].Clone()
        otherHist=tmps[flavor+'_Other'].Clone()
        dataHist=tmps[flavor+'_data_obs'].Clone()
        average(dataHist)
        average(otherHist)
        average(dy_sig)
        average(dy_bkg)
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
        ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0,1,0.3)
        setTDRStyle()
        plotPad.UseCurrentStyle()
        ratioPad.UseCurrentStyle()
        plotPad.Draw()
        ratioPad.Draw()
        plotPad.cd()
        plotPad.SetLogy()
        plotPad.SetLogx()
        plotPad.SetBottomMargin(0.14)
        Stack.Draw("hist")
        Stack.GetYaxis().SetTitle('Event/GeV')
        Stack.GetXaxis().SetLabelSize(0.0)
        Stack.GetXaxis().SetMoreLogLabels()
        Stack.SetMinimum(5e-4)
        Stack.SetMaximum(5e4)
        Stack.GetXaxis().SetLimits(150, 3500)
        Stack.GetXaxis().SetRangeUser(150,3500)
        if flavor == "el": Stack.SetTitle("dielectron"+" "+year+" "+cg)
        else: Stack.SetTitle("dimuon"+" "+year+" "+cg)
        dataHist.SetMarkerStyle(8)
        dataHist.SetLineColor(1)
        dataHist.Draw("samep")
        ly.SetBorderSize(0)
        ly.Draw()
        ratioPad.cd()
        ratioPad.SetLogx()
        ratioPad.SetTopMargin(0.025)
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
        ratioHist.GetYaxis().SetTitleSize(0.1)
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
        treLine = ROOT.TLine(200, 1.0, 3500, 1.0)
        treLine.SetLineStyle(2)
        treLine.Draw()
        plotPad.cd()
        latexCMS = ROOT.TLatex()
        latexCMS.SetTextSize(0.06)
        latexCMS.SetNDC(True)
        latexCMSExtra = ROOT.TLatex()
        yLabelPos = 0.82
        latexCMSExtra.SetTextSize(0.045)
        latexCMSExtra.SetNDC(True)
        cmsExtra = "Preliminary"
        latex=ROOT.TLatex()
        latex.SetNDC(True)
        latex.SetTextSize(0.025)
        latexCMS.DrawLatex(0.19,0.88,"CMS")
        latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))
        latex.SetTextSize(0.022)
        if year in lumi_mu.keys(): latex.DrawLatex(0.67, 0.96, "%s fb^{-1} (13 TeV, #mu#mu ), %s fb^{-1} (13 TeV, ee)"%(str(int(lumi_mu[year]/1000)),str(int(lumi_el[year]/1000))))
        else: latex.DrawLatex(0.67, 0.96, "140 fb^{-1} (13 TeV, #mu#mu ), 137 fb^{-1} (13 TeV, ee)")
        if fr==1: plotName = flavor+"_"+year+"_"+cg+"_cut"+str(massCut)+"_template.pdf"
        else: plotName = flavor+"_"+year+"_"+cg+"_cut"+str(massCut)+"_"+str(fr)+"fr"+"_template.pdf"
        c.Update()
        c.Print("plots/templates/"+plotName)


