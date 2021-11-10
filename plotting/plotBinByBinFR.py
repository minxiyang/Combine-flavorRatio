import ROOT
import numpy
import math
from setTDRStyle import setTDRStyle
from Parameters import lumi_el, lumi_mu


def plotBinByBinFR(year, cg, bng, med, low, high):


    setTDRStyle()
    c=ROOT.TCanvas("c","c",600,450)
    c.cd()
    mainPad = ROOT.TPad('mainPad','mainPad', 0, 0, 1, 1 )
    mainPad.Draw()
    mainPad.SetFillStyle(0)
    mainPad.cd()
    mainPad.SetTicky()
    mainPad.SetTickx()
    mainPad.SetTopMargin(0.07)
    mainPad.SetBottomMargin(0.12)
    mainPad.SetLeftMargin(0.14)
    mainPad.SetRightMargin(0.063)
    mainPad.SetLogx()
    #h_ratioData.GetXaxis().SetTitle("m [GeV]")
    #h_ratioData.GetXaxis().SetLabelSize(0.055)
    #h_ratioData.GetXaxis().SetLabelOffset(1.05)
    #h_ratioData.GetYaxis().SetTitle("R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{Data} / R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{MC}")
    #h_ratioData.GetYaxis().SetLabelSize(0.055)
    #h_ratioData.GetXaxis().SetLabelOffset(0.01)
    #h_ratioData.GetYaxis().SetRangeUser(0,2)
    #h_ratioData.GetYaxis().SetTickLength(0.025)
    #h_ratioData.SetLineColor(1)
    c.SetLogx()
    g_ratioData=ROOT.TGraphAsymmErrors()
    
    ly=ROOT.TLegend(0.73,0.8,0.92,0.92)
    #ly.AddEntry(g_ratioData, "folded")
    #ly.AddEntry(g_ratioData_cb, "unfolded")
    ly.SetBorderSize(0)


    for i in range(1,len(bng)):
        xval=(bng[i]+bng[i-1])/2.
        xerr_r=xval-bng[i-1]
        xerr_l=bng[i]-xval
        print (high[i-1])
        if high[i-1]==0: high[i-1]=2.
        g_ratioData.SetPoint(i+1, xval, med[i-1])
        g_ratioData.SetPointError(i+1,xerr_r,xerr_l, med[i-1]-low[i-1], high[i-1]-med[i-1])

    latexCMS = ROOT.TLatex()
    latexCMS.SetTextSize(0.06)
    latexCMS.SetNDC(True)
    latex=ROOT.TLatex()
    latex.SetNDC(True)
    latex.SetTextSize(0.025)
    g_ratioData.GetXaxis().SetLabelOffset(1.3)
    g_ratioData.GetXaxis().SetTickLength(0.025)
    g_ratioData.GetXaxis().SetMoreLogLabels()
    g_ratioData.GetXaxis().SetLabelSize(0.04)
    g_ratioData.GetXaxis().SetMaxDigits(10)
    g_ratioData.GetXaxis().SetNdivisions(405)
    g_ratioData.Draw("AP")

    #ly.Draw()
    g_ratioData.GetXaxis().SetRangeUser(200,3500)
    g_ratioData.GetYaxis().SetRangeUser(0,2)
    g_ratioData.GetXaxis().SetTitle("m [GeV]")
    g_ratioData.GetYaxis().SetTitle("R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{Data} / R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{MC}")
    g_ratioData.GetXaxis().SetLabelSize(0.055)
    g_ratioData.GetXaxis().SetLabelOffset(1.05)
    g_ratioData.GetYaxis().SetLabelSize(0.055)
    g_ratioData.GetXaxis().SetLabelOffset(0.01)
    g_ratioData.GetXaxis().SetTickLength(0.025)
    g_ratioData.GetXaxis().SetMoreLogLabels()
    g_ratioData.GetXaxis().SetNoExponent()
    g_ratioData.GetYaxis().SetNdivisions(405)

    #for i in range(3,h_ratioData.GetNbinsX()+1):
    #    chi2Forbe+=((h_ratioData.GetBinContent(i)-1)/h_ratioData.GetBinError(i))**2

    oneLine = ROOT.TLine(200, 1.0, 3500, 1.0)
    oneLine.SetLineStyle(2)
    oneLine.Draw()
    latex.SetTextSize(0.042)
    latex.SetTextFont(42)
    if year in lumi_mu.keys(): latex.DrawLatex(0.38, 0.945, "%s fb^{-1} (13 TeV, #mu#mu ), %s fb^{-1} (13 TeV, ee)"%(str(int(lumi_mu[year]/1000)),str(int(lumi_el[year]/1000))))
    else: latex.DrawLatex(0.38, 0.945, "140 fb^{-1} (13 TeV, #mu#mu ), 137 fb^{-1} (13 TeV, ee)")

    #latex.DrawLatex(0.38, 0.945, "%i fb^{-1} (13 TeV, ee) + %i fb^{-1} (13 TeV, #mu#mu)"%(round((lumi_el[0]+lumi_el[1]+lumi_el[2])*0.001), round((lumi_mu[0]+lumi_mu[1]+lumi_mu[2])*0.001)))
    latex.SetTextSize(0.05)
    if cg == "be":latex.DrawLatex(0.35,0.72,"at least one endcap lepton")
    else: latex.DrawLatex(0.35,0.72,"two barrel leptons")
    latexCMS.SetTextSize(0.07)
    latexCMS.SetTextFont(62)
    latexCMS.DrawLatex(0.18,0.85,"CMS")
    latexCMS.DrawLatex(0.18,0.78,"Preliminary")
    c.Update()
    c.Print("plots/BinByBin/"+year+"_"+cg+"MulitBin_floated.pdf")



