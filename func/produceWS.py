import ROOT
from func.addToWs import addToWs
import numpy as np
from Parameters import data_files


def produceWS(cut):
    rat = {}
    for year in ["2016", "2017", "2018"]:
        for cg in ["bb", "be"]:
            for flavor in ["mu", "el"]:
                ws = ROOT.RooWorkspace(flavor+cg+year)
                for process in ["DY", "Other"]:
                    name=process+"_"+flavor+"_"+year 
                    fileName = "MC/"+name+".root"
                    f = ROOT.TFile.Open(fileName, "read")
                    if flavor == "mu": prefix="Dimuon"
                    else: prefix="Dielectron"
                
                    if process == "DY":
                        histName = prefix+"Response_"
                    elif flavor == "mu": 
                        histName = prefix+"MassVertexConstrained_"
                    else:
                        histName = prefix+"Mass_"

                    if process == "Other":
                        histo = f.Get(histName+cg)
                        rand_histos = []
                        for k in range(5):
                            temphist = histo.Clone(prefix+"Mass_rand"+str(k))
                            temphist.SetDirectory(0)
                            for i in range(histo.GetNbinsX()): 
                                mean = histo.GetBinContent(i)
                                sigma = histo.GetBinError(i)
                                val = np.random.normal(mean, sigma)
                                temphist.SetBinContent(i, val)
                            rand_histos.append(temphist)
                        histo_up = f.Get(histName+cg+"_MassScaleUp")
                        histo_down = f.Get(histName+cg+"_MassScaleDown")
                        #histo_reso = f.Get(histName+cg+"_Smear")
                        if flavor == "mu":
                            histo_reso = f.Get(histName+cg+"_Smear")
                            histo_ID = f.Get(histName+cg+"_MuonID")
                        else:
                            histo_puup = f.Get(histName+cg+"_PUScaleUp")
                            histo_pudown = f.Get(histName+cg+"_PUScaleDown")
                            histo_preup = f.Get(histName+cg+"_PrefireUp")
                            histo_predown = f.Get(histName+cg+"_PrefireDown")
                        #for i in range(0, 150):
                        #    histo.SetBinContent(i, 0)
                        #    histo_up.SetBinContent(i, 0)
                        #    histo_down.SetBinContent(i, 0)
                        #
                        #    if flavor == "mu":
                        #        histo_reso.SetBinContent(i, 0)
                        #        histo_ID.SetBinContent(i, 0)
                        #    else:
                        #        histo_puup.SetBinContent(i, 0)
                        #        histo_pudown.SetBinContent(i, 0)
                        #        histo_preup.SetBinContent(i, 0)
                        #        histo_predown.SetBinContent(i, 0)
                    else:
                          
                        M = f.Get(histName+cg)
                        rand_Ms = []
                        for k in range(5):
                            temphist = M.Clone(prefix+"Response_rand"+str(k))
                            temphist.SetDirectory(0)
                            for i in range(M.GetNbinsX()):
                                for j in range(M.GetNbinsY()):
                                    mean = M.GetBinContent(i, j)
                                    sigma = M.GetBinError(i, j)
                                    val = np.random.normal(mean, sigma)
                                    temphist.SetBinContent(i, j, val)
                            rand_Ms.append(temphist)
                        M_up = f.Get(histName+cg+"_MassScaleUp")
                        M_down = f.Get(histName+cg+"_MassScaleDown")
                        if flavor == "mu":
                            M_reso = f.Get(histName+cg+"_Smear")
                            M_ID = f.Get(histName+cg+"_MuonID")
                        else:
                            M_puup = f.Get(histName+cg+"_PUScaleUp")
                            M_pudown = f.Get(histName+cg+"_PUScaleDown")
                            M_preup = f.Get(histName+cg+"_PrefireUp")
                            M_predown = f.Get(histName+cg+"_PrefireDown")
                        
                        histo = M.ProjectionX(prefix+"1" ,cut/10+1, -1)
                        histo_up = M_up.ProjectionX(prefix+"2", cut/10+1, -1)  
                        histo_down = M_down.ProjectionX(prefix+"3", cut/10+1, -1)
                        histo_b = M.ProjectionX(prefix+"4", 15, cut/10)
                        histo_up_b = M_up.ProjectionX(prefix+"5", 15, cut/10)
                        histo_down_b = M_down.ProjectionX(prefix+"6", 15, cut/10)
                        rand_histos = []
                        rand_histos_b = []
                        for k in range(5):
                            rand_M = rand_Ms[k]
                            temp = rand_M.ProjectionX(prefix+"_rand"+str(k) ,cut/10+1, -1)
                            temp_b = rand_M.ProjectionX(prefix+"_randb"+str(k), 15, cut/10)
                            rand_histos.append(temp)
                            rand_histos_b.append(temp_b)
                        if flavor == "mu":
                            histo_reso_b = M_reso.ProjectionX(prefix+"7", 15, cut/10)
                            histo_reso = M_reso.ProjectionX(prefix+"8", cut/10+1, -1)
                            histo_ID = M_ID.ProjectionX(prefix+"9", cut/10+1, -1)
                            histo_ID_b = M_ID.ProjectionX(prefix+"10", 15, cut/10)
                        else:
                            histo_puup = M_puup.ProjectionX(prefix+"11", cut/10+1, -1)
                            histo_puup_b = M_puup.ProjectionX(prefix+"12", 15, cut/10)
                            histo_pudown = M_pudown.ProjectionX(prefix+"13", cut/10+1, -1)
                            histo_pudown_b = M_pudown.ProjectionX(prefix+"14", 15, cut/10)
                            histo_preup = M_preup.ProjectionX(prefix+"15", cut/10+1, -1)
                            histo_preup_b = M_preup.ProjectionX(prefix+"16", 15, cut/10)
                            histo_predown = M_predown.ProjectionX(prefix+"17", cut/10+1, -1)
                            histo_predown_b = M_predown.ProjectionX(prefix+"18", 15, cut/10)
                    
                    '''
                    for i in range(0, 150):
                            histo.SetBinContent(i, 0)
                            histo_up.SetBinContent(i, 0)
                            histo_down.SetBinContent(i, 0)

                            if flavor == "mu":
                                histo_reso.SetBinContent(i, 0)
                                histo_ID.SetBinContent(i, 0)
                            else:
                                histo_puup.SetBinContent(i, 0)
                                histo_pudown.SetBinContent(i, 0)
                                histo_preup.SetBinContent(i, 0)
                                histo_predown.SetBinContent(i, 0)
                    '''
                    for i in range(1, histo.GetNbinsX()+1):
                        if histo.GetBinContent(i)<0: histo.SetBinContent(i, 0)
                        if histo_up.GetBinContent(i)<0: histo_up.SetBinContent(i, 0)
                        if histo_down.GetBinContent(i)<0: histo_down.SetBinContent(i, 0)
                        if flavor == "mu":
                            if histo_ID.GetBinContent(i)<0: histo_ID.SetBinContent(i, 0)
                            if histo_reso.GetBinContent(i)<0: histo_reso.SetBinContent(i, 0)
                        else:
                            if histo_puup.GetBinContent(i)<0: histo_puup.SetBinContent(i, 0)
                            if histo_preup.GetBinContent(i)<0: histo_preup.SetBinContent(i, 0)
                            if histo_pudown.GetBinContent(i)<0: histo_pudown.SetBinContent(i, 0)
                            if histo_predown.GetBinContent(i)<0: histo_predown.SetBinContent(i, 0)
                        if process == "DY":

                            if histo_b.GetBinContent(i)<0: histo_b.SetBinContent(i, 0)
                            if histo_up_b.GetBinContent(i)<0: histo_up_b.SetBinContent(i, 0)
                            if histo_down_b.GetBinContent(i)<0: histo_down_b.SetBinContent(i, 0)
                            if flavor == "mu":
                                if histo_ID_b.GetBinContent(i)<0: histo_ID_b.SetBinContent(i, 0)
                                if histo_reso_b.GetBinContent(i)<0: histo_reso_b.SetBinContent(i, 0)
                            else:
                                if histo_puup_b.GetBinContent(i)<0: histo_puup_b.SetBinContent(i, 0)
                                if histo_preup_b.GetBinContent(i)<0: histo_preup_b.SetBinContent(i, 0)
                                if histo_pudown_b.GetBinContent(i)<0: histo_pudown_b.SetBinContent(i, 0)
                                if histo_predown_b.GetBinContent(i)<0: histo_predown_b.SetBinContent(i, 0)
                       
                    if process == "DY":
                        binsize = 25
                        histo = histo.Rebin(binsize, histo.GetName())
                        rands = []
                        rands_b = []
                        for i in range(5):
                           
                            temp = rand_histos[i].Rebin(binsize, rand_histos[i].GetName())
                            rands.append(temp)
                            temp = rand_histos_b[i].Rebin(binsize, rand_histos_b[i].GetName())
                            rands_b.append(temp)
      

                        histo_up = histo_up.Rebin(binsize, histo_up.GetName())
                        histo_down = histo_down.Rebin(binsize, histo_down.GetName())
                        histo_b = histo_b.Rebin(binsize, histo_b.GetName())
                        histo_up_b = histo_up_b.Rebin(binsize, histo_up_b.GetName())
                        histo_down_b = histo_down_b.Rebin(binsize, histo_down_b.GetName())
                        
                        if flavor == "mu":
                            histo_ID = histo_ID.Rebin(binsize, histo_ID.GetName())
                            histo_ID_b = histo_ID_b.Rebin(binsize, histo_ID_b.GetName())
                            histo_reso = histo_reso.Rebin(binsize, histo_reso.GetName())
                            histo_reso_b = histo_reso_b.Rebin(binsize, histo_reso_b.GetName())
                        else:
                            histo_puup = histo_puup.Rebin(binsize, histo_puup.GetName())
                            histo_pudown = histo_pudown.Rebin(binsize, histo_pudown.GetName())
                            histo_preup = histo_preup.Rebin(binsize, histo_preup.GetName())
                            histo_predown = histo_predown.Rebin(binsize, histo_predown.GetName())
                            histo_puup_b = histo_puup_b.Rebin(binsize, histo_puup_b.GetName())
                            histo_pudown_b = histo_pudown_b.Rebin(binsize, histo_pudown_b.GetName())
                            histo_preup_b = histo_preup_b.Rebin(binsize, histo_preup_b.GetName())
                            histo_predown_b = histo_predown_b.Rebin(binsize, histo_predown_b.GetName())
                 
                        histo_b.SetDirectory(0)
                        histo_up_b.SetDirectory(0)
                        histo_down_b.SetDirectory(0)
                        if flavor == "mu":
                            histo_ID_b.SetDirectory(0)
                            histo_reso_b.SetDirectory(0)
                        else:
                            histo_puup_b.SetDirectory(0)
                            histo_pudown_b.SetDirectory(0)
                            histo_preup_b.SetDirectory(0)
                            histo_predown_b.SetDirectory(0)

                    else:
                        bins = [150, 175, 200, 240, 280, 320, 360, 400,  500,  600, 700, 900, 1300, 1800, 3500] 
                        bngs = np.asarray(bins, dtype=np.float64)
                        histo = histo.Rebin(len(bngs)-1, histo.GetName(), bngs)
                        rands = []
                        for i in range(5):
                        
                            temp = rand_histos[i].Rebin(len(bngs)-1, rand_histos[i].GetName(), bngs)
                            rands.append(temp)
                        histo_up = histo_up.Rebin(len(bngs)-1, histo_up.GetName(), bngs)
                        histo_down = histo_down.Rebin(len(bngs)-1, histo_down.GetName(), bngs)
                        if flavor == "mu":
                            histo_ID = histo_ID.Rebin(len(bngs)-1, histo_ID.GetName(), bngs)
                            histo_reso = histo_reso.Rebin(len(bngs)-1, histo_reso.GetName(), bngs)
                        else:
                            histo_puup = histo_puup.Rebin(len(bngs)-1, histo_puup.GetName(), bngs)
                            histo_pudown = histo_pudown.Rebin(len(bngs)-1, histo_pudown.GetName(), bngs)
                            histo_preup = histo_preup.Rebin(len(bngs)-1, histo_preup.GetName(), bngs)
                            histo_predown = histo_predown.Rebin(len(bngs)-1, histo_predown.GetName(), bngs)

                    histo.SetDirectory(0)
                    histo_up.SetDirectory(0)
                    histo_down.SetDirectory(0)
                  
                    if flavor == "mu":
                        histo_reso.SetDirectory(0)
                        histo_ID.SetDirectory(0)
                    else:
                        histo_puup.SetDirectory(0)
                        histo_pudown.SetDirectory(0)
                        histo_preup.SetDirectory(0)
                        histo_predown.SetDirectory(0)
                    prefix=flavor+cg+year+"_"+process
                    for rand in rands: rand.SetDirectory(0)
                    if process == "DY":
                        for rand in rands_b: rand.SetDirectory(0)
                    f.Close()
                    print(flavor+year+cg+process)
                    y1 = histo.Integral()
                    y2 = histo_up.Integral()
                    y3 = histo_down.Integral()
                    if flavor == "mu":
                        y4 = histo_reso.Integral()
                        y5 = histo_ID.Integral()
                        print((y1,y2,y3,y4,y5))
                    else:
                        y4 = histo_puup.Integral()
                        y5 = histo_pudown.Integral()
                        y6 = histo_preup.Integral()
                        y7 = histo_predown.Integral()
                        print((y1,y2,y3,y4,y5,y6,y7))
                    if process=="DY":
                        y1 = histo_b.Integral()
                        y2 = histo_up_b.Integral()
                        y3 = histo_down_b.Integral()
                        if flavor == "mu":
                            y4 = histo_reso_b.Integral()
                            y5 = histo_ID_b.Integral()
                            print((y1,y2,y3,y4,y5))
                        else:
                            y4 = histo_puup_b.Integral()
                            y5 = histo_pudown_b.Integral()
                            y6 = histo_preup_b.Integral()
                            y7 = histo_predown_b.Integral()
                            print((y1,y2,y3,y4,y5,y6,y7))


                    if process=="DY":
                        massVar = ROOT.RooRealVar(prefix+"_mass", prefix+"_mass", 150., 3500.)
                        addToWs(ws, massVar)
                        varName_sig = prefix+"_sig"
                        varName_bkg = prefix+"_bkg"
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

                        m_arg=ROOT.RooArgSet(ws.var(prefix+"_mass"), "m_arg")
                        dataset=ROOT.RooDataSet("data_obs", "data_obs", m_arg)
                        nev=0
                        for m in data:
                            if  m<3500 and m>150:
                                nev+=1
                                m = ROOT.Double(m) 
                                ROOT.RooAbsRealLValue.__assign__(ws.var(prefix+"_mass"), m)
                                dataset.add(m_arg, 1.0)

                        addToWs(ws, dataset)
                        f.close()
                        print (nev)
                    datahist = ROOT.RooDataHist(prefix+"Mass_"+cg, prefix+"Mass_"+cg, ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo))
                    histpdf = ROOT.RooHistPdf(prefix+"pdf_"+cg, prefix+"pdf_"+cg, ROOT.RooArgSet(massVar), datahist) 
                    datahist_up = ROOT.RooDataHist(prefix+"Mass_"+cg+"_scaleUp", prefix+"Mass_"+cg+"_scaleUp", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_up))
                    histpdf_up = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_scaleUp", prefix+"pdf_"+cg+"_scaleUp", ROOT.RooArgSet(massVar), datahist_up)
                    datahist_down = ROOT.RooDataHist(prefix+"Mass_"+cg+"_scaleDown", prefix+"Mass_"+cg+"_scaleDown", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_down))
                    histpdf_down = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_scaleDown", prefix+"pdf_"+cg+"_scaleDown", ROOT.RooArgSet(massVar), datahist_down)
                    i = 0
                    for i in range(5):
                        
                        datarand = ROOT.RooDataHist(prefix+"Mass_"+cg+"_rand"+str(i), prefix+"Mass_"+cg+"_rand"+str(i), ROOT.RooArgList(massVar), ROOT.RooFit.Import(rands[i]))
                        randpdf = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_rand"+str(i), prefix+"pdf_"+cg+"_rand"+str(i), ROOT.RooArgSet(massVar), datarand)
                        addToWs(ws, randpdf)
                    if flavor == "mu":
                        datahist_ID = ROOT.RooDataHist(prefix+"Mass_"+cg+"_ID", prefix+"Mass_"+cg+"_ID", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_ID))
                        histpdf_ID = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_ID", prefix+"pdf_"+cg+"_ID", ROOT.RooArgSet(massVar), datahist_ID)
                        datahist_reso = ROOT.RooDataHist(prefix+"Mass_"+cg+"_smear", prefix+"Mass_"+cg+"_smear", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_reso))
                        histpdf_reso = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_smear", prefix+"pdf_"+cg+"_smear", ROOT.RooArgSet(massVar), datahist_reso)
                        addToWs(ws, histpdf_reso)
                        if year != "2016" and cg != "be":
                            ID_var = ROOT.RooRealVar("IDvar", "IDvar", 0, -4.0, 4.0)
                        else:
                            ID_var = ROOT.RooRealVar(flavor+"_"+year+"_"+cg+"_IDvar", flavor+"_"+year+"_"+cg+"_IDvar", 0, -4.0, 4.0)
                        if year !="2016":
                            mass_var =  ROOT.RooRealVar("massvar", "massvar", 0, -4.0, 4.0)
                        else:
                            mass_var = ROOT.RooRealVar(flavor+"_"+year+"_"+cg+"_massvar", flavor+"_"+year+"_"+cg+"_massvar", 0, -4.0, 4.0)
                        func1 = ROOT.RooFormulaVar(prefix+"func1"+cg, prefix+"func1"+cg, "1. - (abs(@0)<1)*0.125*(3*@0*@0*@0*@0*@0*@0 - 10*@0*@0*@0*@0+15*@0*@0) -(abs(@1)<1)*0.125*(3*@1*@1*@1*@1*@1*@1 - 10*@1*@1*@1*@1+15*@1*@1) - (abs(@0)>1)*abs(@0) - (abs(@1)>1)*abs(@1)", ROOT.RooArgList(mass_var,ID_var))
                        func2 = ROOT.RooFormulaVar(prefix+"func2"+cg, prefix+"func2"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 + @0) + (@0>1)*@0", ROOT.RooArgList(mass_var))
                        func3 = ROOT.RooFormulaVar(prefix+"func3"+cg, prefix+"func3"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 - @0) - (@0<-1)*@0", ROOT.RooArgList(mass_var))
                        func4 = ROOT.RooFormulaVar(prefix+"func4"+cg, prefix+"func4"+cg, "(abs(@0)<1)*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0) + (abs(@0)>1)*abs(@0)", ROOT.RooArgList(ID_var))

                        extra = ROOT.RooAddPdf(prefix+"pdf_"+cg+"_extra", prefix+"pdf_"+cg+"_extra", ROOT.RooArgList(histpdf, histpdf_up, histpdf_down, histpdf_ID), ROOT.RooArgList(func1, func2, func3, func4))
                        addToWs(ws, extra)
                    else:
                        
                        datahist_puup = ROOT.RooDataHist(prefix+"Mass_"+cg+"_puup", prefix+"Mass_"+cg+"_puup", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_puup))
                        histpdf_puup = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_puup", prefix+"pdf_"+cg+"_puup", ROOT.RooArgSet(massVar), datahist_puup)
                        datahist_preup = ROOT.RooDataHist(prefix+"Mass_"+cg+"_preup", prefix+"Mass_"+cg+"_preup", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_preup))
                        histpdf_preup = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_preup", prefix+"pdf_"+cg+"_preup", ROOT.RooArgSet(massVar), datahist_preup)
                        datahist_pudown = ROOT.RooDataHist(prefix+"Mass_"+cg+"_pudown", prefix+"Mass_"+cg+"_pudown", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_pudown))
                        histpdf_pudown = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_pudown", prefix+"pdf_"+cg+"_pudown", ROOT.RooArgSet(massVar), datahist_pudown)
                        datahist_predown = ROOT.RooDataHist(prefix+"Mass_"+cg+"_predown", prefix+"Mass_"+cg+"_predown", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_predown))
                        histpdf_predown = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_predown", prefix+"pdf_"+cg+"_predown", ROOT.RooArgSet(massVar), datahist_predown)
                        addToWs(ws, histpdf_puup)
                        addToWs(ws, histpdf_pudown)
                        addToWs(ws, histpdf_preup)
                        addToWs(ws, histpdf_predown)
                        func1 = ROOT.RooFormulaVar(prefix+"func1"+cg, prefix+"func1"+cg, "1. - (abs(@0)<1)*0.125*(3*@0*@0*@0*@0*@0*@0 - 10*@0*@0*@0*@0+15*@0*@0) - (abs(@0)>1)*abs(@0)", ROOT.RooArgList(mass_var))
                        func2 = ROOT.RooFormulaVar(prefix+"func2"+cg, prefix+"func2"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 + @0)+ (@0>1)*@0", ROOT.RooArgList(mass_var))
                        func3 = ROOT.RooFormulaVar(prefix+"func3"+cg, prefix+"func3"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 - @0)- (@0<-1)*@0", ROOT.RooArgList(mass_var))

                        extra = ROOT.RooAddPdf(prefix+"pdf_"+cg+"_extra", prefix+"pdf_"+cg+"_extra", ROOT.RooArgList(histpdf, histpdf_up, histpdf_down), ROOT.RooArgList(func1, func2, func3))
                        addToWs(ws, extra)
                    if process == "DY":
                        #c=ROOT.TCanvas('c', 'c', 800, 800)
                        #frame1 = massVar.frame()
                        #frame1.SetTitle("Morph plot")
                        #frame1.GetXaxis().SetTitle("mll [GeV]")
                        #frame1.GetYaxis().SetTitle("arb. unit")
                        #histpdf.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kBlue), ROOT.RooFit.LineWidth(1))
                        #histpdf_up.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kGreen), ROOT.RooFit.LineWidth(1))
                        #histpdf_down.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kBlue), ROOT.RooFit.LineWidth(1))
                        #mass_var.setVal(0)
                        #extra.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1), ROOT.RooFit.LineStyle(2))
                        #mass_var.setVal(-0.5)
                        #extra.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1), ROOT.RooFit.LineStyle(2))
                        #mass_var.setVal(0.5)
                        #extra.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1), ROOT.RooFit.LineStyle(2))
                        #mass_var.setVal(-1)
                        #extra.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1), ROOT.RooFit.LineStyle(2))
                        #mass_var.setVal(1)
                        #extra.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(1), ROOT.RooFit.LineStyle(2))

                        #histpdf.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kBlue), ROOT.RooFit.LineWidth(1))
                        #histpdf_up.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kGreen), ROOT.RooFit.LineWidth(1))
                        #histpdf_down.plotOn(frame1, ROOT.RooFit.LineColor(ROOT.kGreen), ROOT.RooFit.LineWidth(1))
                        #frame1.Draw()
                        #c.Print(prefix+"Mass_"+cg+".pdf")
                        datahist_b = ROOT.RooDataHist(prefix+"Mass_"+cg, prefix+"Mass_"+cg, ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_b))
                        histpdf_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_bkg", prefix+"pdf_"+cg+"_bkg", ROOT.RooArgSet(massVar), datahist_b)
                        datahist_up_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_scaleUp", prefix+"Mass_"+cg+"_scaleUp", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_up_b))
                        histpdf_up_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_scaleUp_bkg", prefix+"pdf_"+cg+"_scaleUp_bkg", ROOT.RooArgSet(massVar), datahist_up_b)
                        datahist_down_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_scaleDown", prefix+"Mass_"+cg+"_scaleDown", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_down_b))
                        histpdf_down_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_scaleDown_bkg", prefix+"pdf_"+cg+"_scaleDown_bkg", ROOT.RooArgSet(massVar), datahist_down_b)
                        i = 0
                        for i in range(5):
                            
                            datarand = ROOT.RooDataHist(prefix+"Mass_"+cg+"_rand"+str(i)+"_bkg", prefix+"Mass_"+cg+"_rand"+str(i)+"_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(rands_b[i]))
                            randpdf = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_rand"+str(i)+"_bkg", prefix+"pdf_"+cg+"_rand"+str(i)+"_bkg", ROOT.RooArgSet(massVar), datarand)
                            addToWs(ws, randpdf)
                        if flavor == "mu":
                            datahist_ID_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_ID_bkg", prefix+"Mass_"+cg+"_ID_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_ID_b))
                            histpdf_ID_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_ID_bkg", prefix+"pdf_"+cg+"_ID_bkg", ROOT.RooArgSet(massVar), datahist_ID_b)
                            datahist_reso_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_smear_bkg", prefix+"Mass_"+cg+"_smear_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_reso_b))
                            histpdf_reso_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_smear_bkg", prefix+"pdf_"+cg+"_smear_bkg", ROOT.RooArgSet(massVar), datahist_reso_b)
                            addToWs(ws, histpdf_reso_b)
                            func1_b = ROOT.RooFormulaVar(prefix+"func1_bkg"+cg, prefix+"func1_bkg"+cg, "1. - (abs(@0)<1)*0.125*(3*@0*@0*@0*@0*@0*@0 - 10*@0*@0*@0*@0+15*@0*@0) -(abs(@1)<1)*0.125*(3*@1*@1*@1*@1*@1*@1 - 10*@1*@1*@1*@1+15*@1*@1) - (abs(@0)>1)*abs(@0) - (abs(@1)>1)*abs(@1)", ROOT.RooArgList(mass_var,ID_var))
                            func2_b = ROOT.RooFormulaVar(prefix+"func2_bkg"+cg, prefix+"func2_bkg"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 + @0) + (@0>1)*@0", ROOT.RooArgList(mass_var))
                            func3_b = ROOT.RooFormulaVar(prefix+"func3_bkg"+cg, prefix+"func3_bkg"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 - @0) - (@0<-1)*@0", ROOT.RooArgList(mass_var))
                            func4_b = ROOT.RooFormulaVar(prefix+"func4_bkg"+cg, prefix+"func4_bkg"+cg, "(abs(@0)<1)*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0) + (abs(@0)>1)*abs(@0)", ROOT.RooArgList(ID_var))
                            extra_b = ROOT.RooAddPdf(prefix+"pdf_"+cg+"_extra_bkg", prefix+"pdf_"+cg+"_extra_bkg", ROOT.RooArgList(histpdf_b, histpdf_up_b, histpdf_down_b, histpdf_ID_b), ROOT.RooArgList(func1_b, func2_b, func3_b, func4_b))
                            addToWs(ws, extra_b)
                        else:
                            datahist_puup_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_puup_bkg", prefix+"Mass_"+cg+"_puup_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_puup_b))
                            histpdf_puup_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_puup_bkg", prefix+"pdf_"+cg+"_puup_bkg", ROOT.RooArgSet(massVar), datahist_puup_b)
                            datahist_preup_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_preup_bkg", prefix+"Mass_"+cg+"_preup_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_preup_b))
                            histpdf_preup_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_preup_bkg", prefix+"pdf_"+cg+"_preup_bkg", ROOT.RooArgSet(massVar), datahist_preup_b)
                            datahist_pudown_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_pudown_bkg", prefix+"Mass_"+cg+"_pudown_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_pudown_b))
                            histpdf_pudown_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_pudown_bkg", prefix+"pdf_"+cg+"_pudown_bkg", ROOT.RooArgSet(massVar), datahist_pudown_b)
                            datahist_predown_b = ROOT.RooDataHist(prefix+"Mass_"+cg+"_predown_bkg", prefix+"Mass_"+cg+"_predown_bkg", ROOT.RooArgList(massVar), ROOT.RooFit.Import(histo_predown_b))
                            histpdf_predown_b = ROOT.RooHistPdf(prefix+"pdf_"+cg+"_predown_bkg", prefix+"pdf_"+cg+"_predown_bkg", ROOT.RooArgSet(massVar), datahist_predown_b)
                            addToWs(ws, histpdf_puup_b)
                            addToWs(ws, histpdf_pudown_b)
                            addToWs(ws, histpdf_preup_b)
                            addToWs(ws, histpdf_predown_b)
                            func1_b = ROOT.RooFormulaVar(prefix+"func1_bkg"+cg, prefix+"func1_bkg"+cg, "1. - (abs(@0)<1)*0.125*(3*@0*@0*@0*@0*@0*@0 - 10*@0*@0*@0*@0+15*@0*@0) - (abs(@0)>1)*abs(@0)", ROOT.RooArgList(mass_var))
                            func2_b = ROOT.RooFormulaVar(prefix+"func2_bkg"+cg, prefix+"func2_bkg"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 + @0)+ (@0>1)*@0", ROOT.RooArgList(mass_var))
                            func3_b = ROOT.RooFormulaVar(prefix+"func3_bkg"+cg, prefix+"func3_bkg"+cg, "(abs(@0)<1)*0.5*((3./8.)*@0*@0*@0*@0*@0*@0 - 1.25*@0*@0*@0*@0 + (15./8.)*@0*@0 - @0)- (@0<-1)*@0", ROOT.RooArgList(mass_var))
                            extra_b = ROOT.RooAddPdf(prefix+"pdf_"+cg+"_extra_bkg", prefix+"pdf_"+cg+"_extra_bkg", ROOT.RooArgList(histpdf_b, histpdf_up_b, histpdf_down_b), ROOT.RooArgList(func1_b, func2_b, func3_b))
                            addToWs(ws, extra_b)
                ws.writeToFile("datacards/"+flavor+cg+year+"_"+str(cut)+".root")
                ws.Print()
