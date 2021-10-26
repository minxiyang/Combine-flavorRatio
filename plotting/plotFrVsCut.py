import ROOT
import numpy as np




def plotFrVsCut(frLeft2, frLeft1, frMed, frRight1, frRight2, massCut, output):
   
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
    ly = ROOT.TLegend(0.65, 0.7, 0.9, 0.9)
    ly.AddEntry(g_med, "flavor ratio")
    ly.AddEntry(g_sigma1, "1 #sigma envelope")
    ly.AddEntry(g_sigma2, "2 #sigma envelope") 
    ly.Draw()
    g_med.GetXaxis().SetTitle("mass cutoff [GeV]")
    g_med.GetYaxis().SetTitle("flavor ratio")
    g_med.GetXaxis().SetLimits(400, 1100)
    g_med.GetXaxis().SetRangeUser(400, 1100)
    g_med.GetYaxis().SetRangeUser(0, 2)
    treLine = ROOT.TLine(400, 1.0, 1100, 1.0)
    treLine.SetLineStyle(2)
    treLine.Draw()
    c.Update()
    c.Print("plots/frVsMasscut/"+output+".pdf")
    




