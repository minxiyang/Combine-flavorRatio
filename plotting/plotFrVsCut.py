import ROOT
import numpy as np
from plotting.setTDRStyle import setTDRStyle
from Parameters import lumi_el, lumi_mu


def plotFrVsCut(frLeft2, frLeft1, frMed, frRight1, frRight2, massCut, output):
    setTDRStyle()
    ROOT.gStyle.SetOptStat(0) 
    frLeft2=np.asarray(frLeft2, dtype=np.float64)
    frLeft1=np.asarray(frLeft1, dtype=np.float64)
    frRight2=np.asarray(frRight2, dtype=np.float64)
    frRight1=np.asarray(frRight1, dtype=np.float64)
    frMed=np.asarray(frMed, dtype=np.float64)
    massCut=np.asarray(massCut, dtype=np.float64)
    
    g_med=ROOT.TGraph(len(massCut), massCut, frMed)
    g_med.SetLineColor(1)
    g_sigma1=ROOT.TGraph(int(2*len(massCut)), np.concatenate([massCut, massCut[::-1]]), np.concatenate([frRight1, frLeft1[::-1]]))            
    g_sigma1.SetFillColorAlpha(3, 0.5)
    g_sigma2=ROOT.TGraph(int(2*len(massCut)), np.concatenate([massCut, massCut[::-1]]), np.concatenate([frRight2, frLeft2[::-1]]))
    g_sigma2.SetFillColorAlpha(5, 0.5)

    c=ROOT.TCanvas("c", "c", 800, 800)
    g_med.Draw("al")
    g_sigma2.Draw("f")
    g_sigma1.Draw("f")
    ly = ROOT.TLegend(0.75, 0.8, 0.9, 0.9)
    ly.SetTextSize(0.03)
    ly.SetBorderSize(0)
    ly.AddEntry(g_med, "flavor ratio")
    ly.AddEntry(g_sigma1, "1 #sigma envelope")
    ly.AddEntry(g_sigma2, "2 #sigma envelope") 
    ly.Draw()
    g_med.GetXaxis().SetTitle("mass cutoff [GeV]")
    g_med.GetYaxis().SetTitle("flavor ratio")
    g_med.GetXaxis().SetTitleSize(0.04)
    g_med.GetYaxis().SetTitleSize(0.04)
    g_med.GetXaxis().SetLimits(400, 1200)
    g_med.GetXaxis().SetRangeUser(400, 1200)
    g_med.GetYaxis().SetRangeUser(0, 2.5)
    treLine = ROOT.TLine(400, 1.0, 1200, 1.0)
    treLine.SetLineStyle(2)
    treLine.Draw()
    latexCMS = ROOT.TLatex()
    latexCMS.SetTextFont(61)
    latexCMS.SetNDC(True)
    latexCMS.SetTextSize(0.06)
    latexCMS.DrawLatex(0.19,0.88,"CMS")
    latexCMS.SetTextSize(0.045)
    latexCMS.DrawLatex(0.19,0.82,"Preliminary")
    latex = ROOT.TLatex()
    latex.SetTextFont(42)
    latex.SetTextAlign(31)
    latex.SetTextSize(0.022)
    latex.SetNDC(True)
    if "2018" in output: year="2018"
    elif "2017" in output: year="2017"
    elif "2016" in output: year="2016"
    else: year="all"
    if year in lumi_mu.keys(): latex.DrawLatex(0.9, 0.96, "%s fb^{-1} (13 TeV, #mu#mu ), %s fb^{-1} (13 TeV, ee)"%(str(int(lumi_mu[year]/1000)),str(int(lumi_el[year]/1000))))
    else: latex.DrawLatex(0.9, 0.96, "140 fb^{-1} (13 TeV, #mu#mu ), 137 fb^{-1} (13 TeV, ee)")

    c.Update()
    c.Print("plots/frVsMasscut/"+output+".pdf")
    




