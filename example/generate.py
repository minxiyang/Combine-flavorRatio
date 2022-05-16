import numpy as np
import ROOT


def main():

    Nbkg = 10000
    Nsig = 500
    nbkg = np.random.poisson(Nbkg, 1)
    nsig = np.random.poisson(Nsig, 1)
    bkgs = np.random.exponential(100, nbkg)
    sigs = np.random.normal(50, 5, nsig)

    h_data = ROOT.TH1D("data_obs", "toy data", 100, 0, 100)
    h_bkg = ROOT.TH1D("bkg", "", 100, 0, 100)
    h_sig = ROOT.TH1D("sig", "", 100, 0, 100)

    for x in range(1, 101):

        val = 100.*np.exp(-x/100.)
        h_bkg.SetBinContent(x, val)
        val = (500./(5*np.sqrt(2*np.pi)))*np.exp(-(x-50)**2/50.)
        h_sig.SetBinContent(x, val)
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
    stack.Draw("hist")
    h_data.Draw("samep")
    c.Print("example.pdf")

    print("observed data is:")
    print(h_data.Integral(1,101))
    print("signal is:")
    print(h_sig.Integral(1,101))
    print("background is:")
    print(h_bkg.Integral(1,101))

    f = ROOT.TFile.Open("TH1_test.root", "RECREATE")
    h_data.Write()
    h_bkg.Write()
    h_sig.Write()
    f.Close()


    def addToWs(ws, obj):

        getattr(ws, 'import')(obj, ROOT.RooCmdArg())

    data = np.concatenate((sigs, bkgs))
    ws = ROOT.RooWorkspace("WS")
    massVar = ROOT.RooRealVar("massVar", "massVar", 50.0, 0.0, 100.0)
    datahist_TH1 = ROOT.RooDataHist("data_obs", "data_obs", ROOT.RooArgList(massVar), ROOT.RooFit.Import(h_data))
    massVar.setBins(100)
    m_arg=ROOT.RooArgSet(massVar, "m_arg")
    dataset=ROOT.RooDataSet("data", "data", m_arg)
    print(len(data))
    for m in data:
        m = ROOT.Double(m)
        ROOT.RooAbsRealLValue.__assign__(massVar, m)
        dataset.add(m_arg, 1.0)
    datahist = ROOT.RooDataHist("data_obs", "", ROOT.RooArgSet(massVar), dataset)

    c=ROOT.TCanvas('c', 'c', 800, 800)
    frame = massVar.frame()
    frame.SetTitle("")
    frame.GetXaxis().SetTitle("m [GeV]")
    frame.GetYaxis().SetTitle("arb. unit")
    #frame.GetYaxis().SetRangeUser(0, 400)
    
    ly = ROOT.TLegend(0.5, 0.5, 0.8, 0.8)
    ly.SetBorderSize(0)
    histpdf1 = ROOT.RooHistPdf("histpdf1", "histpdf1", ROOT.RooArgSet(massVar), datahist_TH1)
    histpdf2 = ROOT.RooHistPdf("histpdf2", "histpdf2", ROOT.RooArgSet(massVar), datahist)
    histpdf1.plotOn(frame, ROOT.RooFit.Name("TH1"), ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1))
    ly.AddEntry(frame.findObject("TH1"), "created from TH1", "l")
    histpdf2.plotOn(frame, ROOT.RooFit.Name("datahist"), ROOT.RooFit.LineColor(ROOT.kGreen), ROOT.RooFit.LineWidth(1))
    ly.AddEntry(frame.findObject("datahist"), "created from RooDataset and setbins", "l")
    #frame.GetYaxis().SetRangeUser(0, 400)
    frame.Draw()
    ly.Draw()
    c.Print("datahistVsTH1.pdf")
    sighist = ROOT.RooDataHist("sighist", "sighist", ROOT.RooArgList(massVar), ROOT.RooFit.Import(h_sig))
    sigpdf = ROOT.RooHistPdf("sig", "sig", ROOT.RooArgSet(massVar), sighist)
    bkghist = ROOT.RooDataHist("bkghist", "bkghist", ROOT.RooArgList(massVar), ROOT.RooFit.Import(h_bkg))
    bkgpdf = ROOT.RooHistPdf("bkg", "bkg", ROOT.RooArgSet(massVar), bkghist)
    addToWs(ws, datahist)
    addToWs(ws, sigpdf)
    addToWs(ws, bkgpdf)
    ws.writeToFile("ws_test.root")
    ws.Print()

if __name__=="__main__":
    main()





