import numpy as np
import ROOT


Nbkg = 10000
Nsig = 500
nbkg = np.random.poisson(Nbkg, 1)
nsig = np.random.poisson(Nsig, 1)
bkgs = np.random.exponential(100, nbkg)
sigs = np.random.normal(50, 5, nsig)

h_data = ROOT.TH1D("data_obs", "toy data", 50, 0, 100)
h_bkg = ROOT.TH1D("bkg", "", 50, 0, 100)
h_sig = ROOT.TH1D("sig", "", 50, 0, 100)

for x in range(1, 100, 2):

    val = 100.*np.exp(-x/100.)*2
    h_bkg.SetBinContent((x+1)/2, val)
    val = (500./(5*np.sqrt(2*np.pi)))*np.exp(-(x-50)**2/50.)*2
    h_sig.SetBinContent((x+1)/2, val)
for x in bkgs:
    h_data.Fill(x)

for x in sigs:
    h_data.Fill(x)

h_bkg.SetLineColor(2)
h_sig.SetLineColor(3) 
stack = ROOT.THStack()
stack.Add(h_bkg)
stack.Add(h_sig)
c = ROOT.TCanvas('c', 'c', 800, 800)
h_data.SetMarkerStyle(8)
#h_data.Draw("p")
stack.Draw("hist")
h_data.Draw("samep")
c.Print("example.pdf")


