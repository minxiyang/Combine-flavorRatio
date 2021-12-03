import ROOT as rt

def readhists(ws,inputFileName,histName):
    #histfile = rt.TFile("tmp2018bb_400cut.root","READ")
    histfile = rt.TFile(inputFileName,"READ")
    
    #hist_mu_bkg = histfile.Get("mu_Other")
    #hist_el_bkg = histfile.Get("el_Other")
    hist_mu_bkg = histfile.Get(histName)
    #hist_mu_bkg.Draw()
    print(hist_mu_bkg.Integral())
    datahist = rt.RooDataHist("datahist", "datahist", rt.RooArgList(ws.var("mass")),rt.RooFit.Import(hist_mu_bkg))
    #histfile.Close()
    ws.Import(datahist)


def makePdf(ws, channelName,nbkg):
    #fa1 = rt.TF1("fa1","[0]*exp([1] + [2]*x + [3]*x*x + [4]*x*x*x*x)*pow(x,[5])",0,10)
    #fa1 = rt.TF1("fa1","[0]*exp([1] + [2]*x)*pow(x,[3])",0,10)
    #fa1.SetParameters(1,-1,-1,-1,-1,-1)
    #mass = rt.RooRealVar("mass","mass",400.,3500.)
    bkg_a = rt.RooRealVar("bkg_"+channelName+"_a","bkg_"+channelName+"_a",nbkg, nbkg/10, nbkg*10)
    bkg_b = rt.RooRealVar("bkg_"+channelName+"_b","bkg_"+channelName+"_b",27,0, 120)
    bkg_c = rt.RooRealVar("bkg_"+channelName+"_c","bkg_"+channelName+"_c",-9.025E-3,-0.1, 0.1)
    bkg_d = rt.RooRealVar("bkg_"+channelName+"_d","bkg_"+channelName+"_d",0,-1e-3, 1e-3)
    bkg_e = rt.RooRealVar("bkg_"+channelName+"_e","bkg_"+channelName+"_e",0,-1e-6, 1e-6)
    bkg_f = rt.RooRealVar("bkg_"+channelName+"_f","bkg_"+channelName+"_f",0, 0, 4)
    #bkg_f.setConstant()
    
    #print(d.getVal())

    #bkgmodel = rt.RooGenericPdf("bkgmodel","bkgmodel","@1*exp(@2+@3*(@0-400)+@4*(@0-400)*(@0-400)+@5*(@0-400)*(@0-400)*(@0-400)*(@0-400))*pow((@0-400),@6)",rt.RooArgList(mass,a,b,c,d,e,f))

    bkgmodel = rt.RooGenericPdf("bkgmodel_"+channelName,"bkgmodel_"+channelName,"@1*exp(@2+@3*@0+@4*@0*@0+@5*@0*@0*@0)*pow(@0,@6)",rt.RooArgList(ws.obj("mass"),bkg_a,bkg_b,bkg_c,bkg_d,bkg_e,bkg_f))
    ws.Import(bkgmodel)


def fitresult(ws,channelName,pdfName, datasetName):
    ws.pdf(pdfName).fitTo(ws.data(datasetName),
                          rt.RooFit.Range(400,3500), 
                          rt.RooFit.PrintLevel(-1),
                          rt.RooFit.Verbose(rt.kFALSE))
    print(type(ws.data(datasetName)))
    #ws.pdf(pdfName).fitTo(ws.data(datasetName))
    xframe = ws.var("mass").frame(rt.RooFit.Title("Background Fit"))
    ws.data(datasetName).plotOn(xframe,rt.RooFit.Binning(100))
    #xframe.GetYaxis().SetRangeUser(1E-3, 1E3)
    ws.pdf(pdfName).plotOn(xframe)
    #ws.pdf(pdfName).paramOn(xframe,rt.RooFit.Layout(0.62,0.90),rt.RooFit.Format("NEU",rt.RooFit.AutoPrecision(1)))
    c=rt.TCanvas('c', 'c', 800, 800)
    c.SetLogx()
    c.SetLogy()
    
    xframe.Draw()
    xframe.GetYaxis().SetRangeUser(1E-4, 1E3)
    c.Print("fit2016bbmuon_other.pdf")
    nparam = ws.pdf(pdfName).getParameters(ws.data(datasetName)).getSize()
    print(nparam)
    #chi2 = xframe.chiSquare(ws.pdf(pdfName), ws.data(datasetName), nparam)
    chi2 = xframe.chiSquare()
    print("Fit chi square:", chi2)
    
def createWS(chanName):
    ws = rt.RooWorkspace(chanName+"_ws")
    mass = rt.RooRealVar('mass','mass', 400.0, 3500.)
    ws.Import(mass)
    return ws

def add_dataset(ws, dataset):
    ws.Import(dataset)
def add_obs_data(ws, obsdata):
    ws.Import(obsdata)

def save_workspace(ws, out_name):
    outfile = rt.TFile(out_name+".root", "recreate")
    ws.Write()
    outfile.Close()
    #histfile.Close()
    #fa1.Draw()

def add_signal(ws, templateFilePath):
    Sig_hists = []
    files = []
    list_mass = [400,500,690,900,1250,1610,2000,3500]
    for i in range(len(list_mass)-1):
        files.append(rt.TFile("tmp2016bb_bin"+int(list_mass[i])+"to"+int(list_mass[i+1])))
        Sig_hists.append(files.Get())
        rdh_MC = rt.RooDataHist("rdh_MC","", rt.RooArgList(ws.var("mass")), rt.RooFit.Import(MC_hist)) 
#ras_rdh_MC = r.RooArgSet(rdh_MC)
#rdh_pdf = rt.RooHistPdf("rdh_pdf", "", rt.RooArgSet(x), rdh_MC );
    
if __name__ == "__main__":
    chanName = "bb"
    inputFileName = "MC/Other_mu_2016.root"
    inputHistName = "DimuonMassVertexConstrained_"
    nbkg = 100000
    ws = createWS(chanName)
    readhists(ws, inputFileName, inputHistName+chanName)
    makePdf(ws, chanName, nbkg)
    pdfName = "bkgmodel_"+chanName
    datasetName = "datahist"
    fitresult(ws,chanName, pdfName, datasetName)

    #obs_data_inputFile = rt.TFile("tmp2018bb_400cut.root","READ")
    #data_obs_hist = obs_data_inputFile.Get("mu_data_obs")
    #add_obs_data(ws, data_obs_hist)

    save_workspace(ws, "workspace_"+chanName)
    

   # a = input('Press a key to exit')
   # if a:
   #     exit(0)
