import numpy as np
import ROOT


Nbkg = 5000
Nsig = 300
nbkg = np.random.poisson(Nbkg, 1)
nsig = np.random.poisson(Nsig, 1)
bkgs = np.random.exponential(100, nbkg)
sigs = np.random.normal(50, 10, nsig)

data = ROOT.TH1D("data", "data", 100, 0, 100)

for x in bkgs:
    data.Fill(x)

for x in sigs:
    data.Fill(x)

c = ROOT.TCanvas('c', 'c', 800, 800)
data.SetMarkerSize(8)
data.Draw("p")
c.Print("example.pdf")

