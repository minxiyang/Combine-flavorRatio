from func.doFit import doFit
import ROOT
from func.addToWs import addToWs
import numpy as np
from Parameters import data_files

#ws = ROOT.RooWorkspace("datacards/test_ws.root")
#File = ROOT.TFile.Open("datacards/test_ws.root","recreate")
#ws = ROOT.RooWorkspace("unbinned_ws")
for year in ["2016","2017","2018"]:
    for cg in ["bb", "be"]:
        for flavor in ["mu", "el"]:
            for process in ["DY", "Other"]:
                name=process+"_"+flavor+"_"+year 
                fitR = doFit(name, flavor, cg, year)
                fileName = "MC/"+name+".root"
                f = ROOT.TFile.Open(fileName, "read")
                if flavor == "mu": prefix="Dimuon"
                else: prefix="Dielectron"

                if process == "DY":
                    reM = f.Get(prefix+"Response_"+cg)
                    reM.SetDirectory(0)
                    f.Close()
                    histo = reM.ProjectionY()
                    Yield = histo.Integral(400, -1)
                    mass = range(405, 3500, 10)
                    mass = np.asarray(mass)
                else:
                    if flavor == "mu": histo = f.Get(prefix+"MassVertexConstrained_"+cg)
                    else: histo = f.Get(prefix+"Mass_"+cg)
                    histo.SetDirectory(0)
                    f.Close()
                    histo.Sumw2()
                    Yield = histo.Integral(400, -1)
                prefix=flavor+cg+year
                if process == "DY": ws = ROOT.RooWorkspace(prefix)
                #massVarName=year+flavor+"mass"
                massVar = ROOT.RooRealVar(prefix+"_mass", prefix+"_mass", 400.0, 3500.) 
                addToWs(ws, massVar)
                if process == "DY": varName = prefix+"_sig"
                else: varName = prefix+"_bkg"
                fac = 0.01
                par1 = ROOT.RooRealVar(varName+"_par1", varName+"_par1", fitR["param"][0], fitR["param"][0]-fac*abs(fitR["param"][0]), fitR["param"][0]+fac*abs(fitR["param"][0]))
                par2 = ROOT.RooRealVar(varName+"_par2", varName+"_par2", fitR["param"][1], fitR["param"][1]-fac*abs(fitR["param"][1]), fitR["param"][1]+fac*abs(fitR["param"][1]))
                par3 = ROOT.RooRealVar(varName+"_par3", varName+"_par3", fitR["param"][2], fitR["param"][2]-fac*abs(fitR["param"][2]), fitR["param"][2]+fac*abs(fitR["param"][2]))
                par4 = ROOT.RooRealVar(varName+"_par4", varName+"_par4", fitR["param"][3], fitR["param"][3]-fac*abs(fitR["param"][3]), fitR["param"][3]+fac*abs(fitR["param"][3]))
                par5 = ROOT.RooRealVar(varName+"_par5", varName+"_par5", fitR["param"][4], fitR["param"][4]-fac*abs(fitR["param"][4]), fitR["param"][4]+fac*abs(fitR["param"][4]))      

                model = ROOT.RooGenericPdf(varName+"model", varName+"model", "@1*exp(@3*@0+@4*@0*@0+@5*@0*@0*@0)*pow(@0,@2)",ROOT.RooArgList(ws.obj(prefix+"_mass"),par1,par2,par3,par4,par5))       
                model_b = ROOT.RooGenericPdf(varName+"model_b", varName+"model_b", "(@0<1000)*@1*exp(@3*@0+@4*@0*@0+@5*@0*@0*@0)*pow(@0,@2)",ROOT.RooArgList(ws.obj(prefix+"_mass"),par1,par2,par3,par4,par5))
                model_s = ROOT.RooGenericPdf(varName+"model_s", varName+"model_s", "(@0>1000)*@1*exp(@3*@0+@4*@0*@0+@5*@0*@0*@0)*pow(@0,@2)",ROOT.RooArgList(ws.obj(prefix+"_mass"),par1,par2,par3,par4,par5))

                addToWs(ws, model)
                addToWs(ws, model_b)
                addToWs(ws, model_s)
                norm = ROOT.RooRealVar(varName+"model_norm",varName+"model_norm", Yield, Yield, Yield)
                norm.setConstant(True)
                addToWs(ws, norm) 
                datahist = ROOT.RooDataHist(varName+"_MC", varName+"_MC", ROOT.RooArgList(ws.var(prefix+"_mass")), ROOT.RooFit.Import(histo))  
                addToWs(ws, datahist)

                fResult=ws.pdf(varName+"model").fitTo(ws.data(varName+"_MC"),
                    ROOT.RooFit.Range(401,3500),
                    ROOT.RooFit.PrintLevel(0),
                    ROOT.RooFit.Verbose(ROOT.kFALSE),
                    ROOT.RooFit.Minimizer("Minuit2","minimize")) 
                norm1=ws.pdf(varName+"model").createIntegral(ROOT.RooArgSet(ws.var(prefix+"_mass"))).getVal() 
                norm1=ws.var(varName+"_par1").getVal()/norm1
                ws.var(varName+"_par1").setVal(norm1)
                ws.var(varName+"_par1").setConstant(True)
                ws.var(varName+"_par2").setConstant(True)
                ws.var(varName+"_par3").setConstant(True)
                ws.var(varName+"_par4").setConstant(True)
                ws.var(varName+"_par5").setConstant(True)

                print("Fit chi square:%s/%s"%(str(fitR["chi2"]),str(fitR["dof"])))
                print("p-value is %s"%str(fitR["pValue"]))
                xframe = ws.var(prefix+"_mass").frame(ROOT.RooFit.Title("data vs fit curve"))  
                if process=="DY":ws.data(varName+"_MC").plotOn(xframe, ROOT.RooFit.Binning(310))
                else:ws.data(varName+"_MC").plotOn(xframe, ROOT.RooFit.Binning(31))
                ws.pdf(varName+"model").plotOn(xframe)
                c1=ROOT.TCanvas('c1', 'c1', 800, 800)
                c1.SetLogy()

                plotPad = ROOT.TPad("plotPad","plotPad",0,0.3,1,1)
                ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0,1,0.3)
                #setTDRStyle()
                plotPad.UseCurrentStyle()
                ratioPad.UseCurrentStyle()
                plotPad.Draw()
                ratioPad.Draw()
                plotPad.cd()
                xframe.Draw()
                xframe.GetYaxis().SetRangeUser(1E-5, 1E4)
                xframe.GetYaxis().SetTitle("fb/GeV")
                xframe.GetYaxis().SetTitleOffset(1.2)
                xframe.GetXaxis().SetTitle("mll [GeV]")
                xframe.SetTitle("data vs fit curve")
                latex=ROOT.TLatex()
                latex.SetTextSize(0.03)
                latex.DrawLatex(2000,3000,"p1*m^{p2}*exp(p3*m+p4*m^{2}+p5*m^{3})")
                latex.DrawLatex(2000,3000/(3.)**1,"p1 = %s \pm %s"%(format(ws.var(varName+"_par1").getVal(), '.3e'), format(ws.var(varName+"_par1").getError(), '.3e')))
                latex.DrawLatex(2000,3000/(3.)**2,"p2 = %s \pm %s"%(format(ws.var(varName+"_par2").getVal(), '.3e'), format(ws.var(varName+"_par2").getError(), '.3e')))
                latex.DrawLatex(2000,3000/(3.)**3,"p3 = %s \pm %s"%(format(ws.var(varName+"_par3").getVal(), '.3e'), format(ws.var(varName+"_par3").getError(), '.3e')))
                latex.DrawLatex(2000,3000/(3.)**4,"p4 = %s \pm %s"%(format(ws.var(varName+"_par4").getVal(), '.3e'), format(ws.var(varName+"_par4").getError(), '.3e')))
                latex.DrawLatex(2000,3000/(3.)**5,"p5 = %s \pm %s"%(format(ws.var(varName+"_par5").getVal(), '.3e'), format(ws.var(varName+"_par5").getError(), '.3e')))
                latex.DrawLatex(2000,3000/(3.)**6,"#chi^{2}/dof = %s/%s"%(format(fitR["chi2"], '.3f'), str(fitR["dof"])))
                latex.DrawLatex(2000,3000/(3.)**7,"p-value = %s"%format(fitR["pValue"], '.3f'))
                plotPad.SetLogy()
                ratioPad.cd()
                pull = xframe.pullHist()
                pull.Draw()
                pull.GetXaxis().SetTitle("mll [GeV]")
                pull.GetYaxis().SetTitle("(Fit/MC - 1)/error")
                pull.GetXaxis().SetRangeUser(400, 3500)
                c1.Print("plots/fitResults/"+varName+prefix+".pdf")
                if process == "DY":
                    files=data_files

                    if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
                    else: files = [file_ for file_ in files if 'ele' in file_]

                    if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
                    elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
                    else:                 files=[file_ for file_ in files if '_2018' in file_]

                    if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
                    else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

                    datafile=files[0]
                    data=[]
                    f=open("dataList/"+datafile,"r")
                    for m in f:

                        m=float(m)
                        data.append(m)
                    f.close()
                    m_arg=ROOT.RooArgSet(ws.var(prefix+"_mass"), "m_arg")
                    dataset=ROOT.RooDataSet("data_obs", "data_obs", m_arg)
  
                    for M in data:
    
                        if M>400 and M<3500: ROOT.RooAbsRealLValue.__assign__(ws.var(prefix+"_mass"), M)
                        dataset.add(m_arg, 1.0)

                    addToWs(ws, dataset)
                if process == "DY":
                    mean = ROOT.RooRealVar(prefix+"_mean", "mean", .0, -2.0, 2.0)
                    sigma = ROOT.RooRealVar(prefix+"_sigma", "sigma", 2, 0.0, 5.0)
                    alpha1 = ROOT.RooRealVar(prefix+"_alpha1", "alpha1", 2, 0.001, 25)
                    n1 = ROOT.RooRealVar(prefix+"_n1", "n1", 1.5, 0, 25)
                    alpha2 = ROOT.RooRealVar(prefix+"_alpha2", "alpha2", 2.0, 0.001, 25)
                    n2 = ROOT.RooRealVar(prefix+"_n2", "n2", 1.5, 0, 25)
                    res_model = ROOT.RooDoubleCB(prefix+"_dcb", "dcb", ws.obj(prefix+"_mass"), mean, sigma, alpha1, n1, alpha2, n2)
                    res_model_s = ROOT.RooDoubleCB(prefix+"_dcb_s", "dcb_s", ws.obj(prefix+"_mass"), mean, sigma, alpha1, n1, alpha2, n2)
                    res_model_b = ROOT.RooDoubleCB(prefix+"_dcb_b", "dcb_b", ws.obj(prefix+"_mass"), mean, sigma, alpha1, n1, alpha2, n2)
                    sigConvDCBmodel = ROOT.RooFFTConvPdf(prefix+"_sigxdcb","Sig(X)dcb",ws.obj(prefix+"_mass"),ws.pdf(varName+"model"), res_model)
                    sigConvDCBmodel_b = ROOT.RooFFTConvPdf(prefix+"_sigxdcb_b","Sig(X)dcb_b",ws.obj(prefix+"_mass"),ws.pdf(varName+"model_b"), res_model_b)
                    sigConvDCBmodel_s = ROOT.RooFFTConvPdf(prefix+"_sigxdcb_s","Sig(X)dcb_s",ws.obj(prefix+"_mass"),ws.pdf(varName+"model_s"), res_model_s)
                    addToWs(ws, sigConvDCBmodel)
                    addToWs(ws, sigConvDCBmodel_b)
                    addToWs(ws, sigConvDCBmodel_s)
                elif process == "Other": 
                    ws.Print()
                    File = ROOT.TFile.Open("datacards/"+prefix+".root","recreate")
                    ws.writeToFile("datacards/"+prefix+".root")
                    File.Close()
