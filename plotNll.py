import ROOT
from math import log
import root_numpy
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='plot significance')
parser.add_argument("--input", action="store", dest="inputRootFile", type=str , default="",help="combine output")
parser.add_argument("--output", action="store", dest="outputPlot", type=str , default="plotNll.pdf",help="plot")
parser.add_argument("--year", action="store", dest="year", type=str , default="2018",help="year")
parser.add_argument("--category", action="store", dest="category", type=str , default="bb",help="category")
args = parser.parse_args()

	
ROOT.gStyle.SetOptStat(0)

f1=ROOT.TFile.Open(args.inputRootFile,"r")
tree_mu=f1.Get("limit")
nllCombine_mu=root_numpy.tree2array(tree_mu,"deltaNLL")
r_mu=root_numpy.tree2array(tree_mu,"r")
Max=np.max(r_mu)
Min=np.min(r_mu)

r=np.linspace(Min, Max,1000)
h_limitCombine1=ROOT.TH1D("hist1","",len(r)-1,r)
h_limitCombine1.GetXaxis().SetTitle('flavor ratio')
h_limitCombine1.GetYaxis().SetTitle('-2#Delta lnL')
h_limitCombine1.SetLineColor(2)

for i in range(1,len(r)): h_limitCombine1.SetBinContent(i,2*nllCombine_mu[i])

c=ROOT.TCanvas("c","c",800,800)

h_limitCombine1.GetYaxis().SetRangeUser(0.0,8.5)
yMax=h_limitCombine1.GetYaxis().GetXmax()
yMin=h_limitCombine1.GetYaxis().GetXmin()
h_limitCombine1.Draw('hist')
treLine = ROOT.TLine(Min, 1.0, Max, 1.0)
treLine.SetLineStyle(2)
treLine.Draw()

latexCMS = ROOT.TLatex()
latexCMS.SetTextFont(61)
latexCMS.SetNDC(True)
latexCMS.SetTextSize(0.04)
latexCMS.DrawLatex(0.13,0.85,"CMS")
latexCMS.DrawLatex(0.13,0.8,"Work in progress")
latex = ROOT.TLatex()
latex.SetTextFont(42)
latex.SetTextAlign(31)
latex.SetTextSize(0.02)
latex.SetNDC(True)
#latex.DrawLatex(0.9, 0.91, "140 fb^{-1} (13 TeV, #mu#mu ), 137 fb^{-1} (13 TeV, ee)")

c.Print(args.outputPlot)


