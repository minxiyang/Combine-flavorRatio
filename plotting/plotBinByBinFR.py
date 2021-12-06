import ROOT
import numpy
import math
from setTDRStyle import setTDRStyle
from Parameters import lumi_el, lumi_mu


def plotBinByBinFR(year, cg, bng, med, low, high, default_FR=[0], default_err=[0]):


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
    c.SetLogx()
    g_ratioData_cb=ROOT.TGraphAsymmErrors()
    g_ratioData_cb.SetMarkerColor(2)
    g_ratioData_cb.SetLineColor(2)
    if len(default_FR)>1:
        g_ratioData=ROOT.TGraphAsymmErrors()
        g_ratioData.SetLineColor(1)
        ly=ROOT.TLegend(0.73,0.8,0.92,0.92)
        ly.AddEntry(g_ratioData_cb, "Likelihood")
        ly.AddEntry(g_ratioData, "Heuristic")
        ly.SetBorderSize(0)


    for i in range(1,len(bng)):
        xval=(bng[i]+bng[i-1])/2.
        xerr_r=xval-bng[i-1]
        xerr_l=bng[i]-xval
        if high[i-1]==0: high[i-1]=3.0
        g_ratioData_cb.SetPoint(i+1, xval*0.98, med[i-1])
        g_ratioData_cb.SetPointError(i+1,xerr_r,xerr_l, med[i-1]-low[i-1], high[i-1]-med[i-1])
        if len(default_FR)>1:
            g_ratioData.SetPoint(i+1,xval,default_FR[i-1])
            g_ratioData.SetPointError(i+1,xerr_r,xerr_l,default_err[i-1],default_err[i-1])

    latexCMS = ROOT.TLatex()
    latexCMS.SetTextSize(0.06)
    latexCMS.SetNDC(True)
    latex=ROOT.TLatex()
    latex.SetNDC(True)
    latex.SetTextSize(0.025)
    g_ratioData_cb.GetXaxis().SetLabelOffset(1.3)
    g_ratioData_cb.GetXaxis().SetTickLength(0.025)
    g_ratioData_cb.GetXaxis().SetMoreLogLabels()
    g_ratioData_cb.GetXaxis().SetLabelSize(0.04)
    g_ratioData_cb.GetXaxis().SetMaxDigits(10)
    g_ratioData_cb.GetXaxis().SetNdivisions(405)
    g_ratioData_cb.Draw("APE0")

    g_ratioData_cb.GetXaxis().SetRangeUser(200,3500)
    g_ratioData_cb.GetYaxis().SetRangeUser(0,3.0)
    g_ratioData_cb.GetXaxis().SetTitle("m [GeV]")
    g_ratioData_cb.GetYaxis().SetTitle("R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{Data} / R_{#mu^{#plus}#mu^{#minus}/e^{#plus}e^{#minus}}^{MC}")
    g_ratioData_cb.GetXaxis().SetLabelSize(0.055)
    g_ratioData_cb.GetXaxis().SetLabelOffset(1.05)
    g_ratioData_cb.GetYaxis().SetLabelSize(0.055)
    g_ratioData_cb.GetXaxis().SetLabelOffset(0.01)
    g_ratioData_cb.GetXaxis().SetTickLength(0.025)
    g_ratioData_cb.GetXaxis().SetMoreLogLabels()
    g_ratioData_cb.GetXaxis().SetNoExponent()
    g_ratioData_cb.GetYaxis().SetNdivisions(405)


    oneLine = ROOT.TLine(200, 1.0, 3500, 1.0)
    oneLine.SetLineStyle(2)
    oneLine.Draw()
    latex.SetTextSize(0.042)
    latex.SetTextFont(42)
    if year in lumi_mu.keys(): latex.DrawLatex(0.38, 0.945, "%s fb^{-1} (13 TeV, #mu#mu ), %s fb^{-1} (13 TeV, ee)"%(str(int(lumi_mu[year]/1000)),str(int(lumi_el[year]/1000))))
    elif year=="Run2": latex.DrawLatex(0.38, 0.945, "140 fb^{-1} (13 TeV, #mu#mu ), 137 fb^{-1} (13 TeV, ee)")
    elif year=="Run2and3": latex.DrawLatex(0.38, 0.945, "300 fb^{-1} (13.6 TeV, #mu#mu ), 300 fb^{-1} (13.6 TeV, ee)")
    else: latex.DrawLatex(0.35, 0.945, "3000 fb^{-1} (14 TeV, #mu#mu ), 3000 fb^{-1} (14 TeV, ee)")
    latex.SetTextSize(0.05)
    if cg == "be":latex.DrawLatex(0.35,0.72,"at least one endcap lepton")
    elif cg == "bb": latex.DrawLatex(0.35,0.72,"two barrel leptons")
    else: latex.DrawLatex(0.35,0.72, "Combined")
    latexCMS.SetTextSize(0.07)
    latexCMS.SetTextFont(62)
    latexCMS.DrawLatex(0.18,0.85,"CMS")
    latexCMS.DrawLatex(0.18,0.78,"Preliminary")
    #g_ratioData_cb.Draw('AP')
    if len(default_FR)>1:
        ly.Draw()
        g_ratioData.Draw('PE0')
    c.Update()
    c.Print("plots/BinByBin/"+year+"_"+cg+"MulitBin_floated.pdf")



