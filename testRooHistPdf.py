import ROOT
from Parameters import data_files
from ROOT import SetOwnership


_file=ROOT.TFile.Open("templates/tmp2018bb_400cut.root")
h_el_DY_S=_file.Get("el_DY_S")
h_el_DY_S.SetDirectory(0)
h_el_DY_S_UP=_file.Get("el_DY_S_2018bb_elMassScaleUp")
h_el_DY_S_UP.SetDirectory(0)
h_el_DY_S_Down=_file.Get("el_DY_S_2018bb_elMassScaleDown")
h_el_DY_S_Down.SetDirectory(0)
h_el_DY_B=_file.Get("el_DY_B")
h_el_DY_B.SetDirectory(0)
h_el_DY_B_UP=_file.Get("el_DY_B_2018bb_elMassScaleUp")
h_el_DY_B_UP.SetDirectory(0)
h_el_DY_B_Down=_file.Get("el_DY_B_2018bb_elMassScaleDown")
h_el_DY_B_Down.SetDirectory(0)
h_el_Other=_file.Get("el_Other")
h_el_Other.SetDirectory(0)
h_el_Other_UP=_file.Get("el_Other_2018bb_elMassScaleUp")
h_el_Other_UP.SetDirectory(0)
h_el_Other_Down=_file.Get("el_Other_2018bb_elMassScaleDown")
h_el_Other_Down.SetDirectory(0)

h_mu_DY_S=_file.Get("mu_DY_S")
h_mu_DY_S.SetDirectory(0)
h_mu_DY_S_UP=_file.Get("mu_DY_S_muMassScaleUp")
h_mu_DY_S_UP.SetDirectory(0)
h_mu_DY_S_Down=_file.Get("mu_DY_S_muMassScaleDown")
h_mu_DY_S_Down.SetDirectory(0)
h_mu_DY_B=_file.Get("mu_DY_B")
h_mu_DY_B.SetDirectory(0)
h_mu_DY_B_UP=_file.Get("mu_DY_B_muMassScaleUp")
h_mu_DY_B_UP.SetDirectory(0)
h_mu_DY_B_Down=_file.Get("mu_DY_B_muMassScaleDown")
h_mu_DY_B_Down.SetDirectory(0)
h_mu_Other=_file.Get("mu_Other")
h_mu_Other.SetDirectory(0)
h_mu_Other_UP=_file.Get("mu_Other_muMassScaleUp")
h_mu_Other_UP.SetDirectory(0)
h_mu_Other_Down=_file.Get("mu_Other_muMassScaleUp")
h_mu_Other_Down.SetDirectory(0)

_file.Close()


x = ROOT.RooRealVar("x","M_{ee}" ,150 , 3500, "GeV")

Roo_mu_DY_S = ROOT.RooDataHist("mu_DY_S","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_S)) 
mu_DY_S = ROOT.RooHistPdf("mu_DY_S", "", ROOT.RooArgSet(x), Roo_mu_DY_S)
SetOwnership(mu_DY_S,False)
Roo_mu_DY_S_UP = ROOT.RooDataHist("mu_DY_S_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_S_UP))     
mu_DY_S_UP = ROOT.RooHistPdf("mu_DY_S_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_mu_DY_S_UP)
SetOwnership(mu_DY_S_UP,False)
Roo_mu_DY_S_Down = ROOT.RooDataHist("mu_DY_S_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_S_Down))
mu_DY_S_Down = ROOT.RooHistPdf("mu_DY_S_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_mu_DY_S_Down)
SetOwnership(mu_DY_S_Down,False)
Roo_mu_DY_B = ROOT.RooDataHist("mu_DY_B","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_B))     
mu_DY_B = ROOT.RooHistPdf("mu_DY_B", "", ROOT.RooArgSet(x), Roo_mu_DY_B)
SetOwnership(mu_DY_B,False)
Roo_mu_DY_B_UP = ROOT.RooDataHist("mu_DY_B_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_B_UP))
mu_DY_B_UP = ROOT.RooHistPdf("mu_DY_B_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_mu_DY_B_UP)
SetOwnership(mu_DY_S_UP,False)
Roo_mu_DY_B_Down = ROOT.RooDataHist("mu_DY_B_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_DY_B_Down))
mu_DY_B_Down = ROOT.RooHistPdf("mu_DY_B_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_mu_DY_B_Down)
SetOwnership(mu_DY_S_Down,False)
Roo_mu_Other = ROOT.RooDataHist("mu_Other","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_Other))
mu_Other = ROOT.RooHistPdf("mu_Other", "", ROOT.RooArgSet(x), Roo_mu_Other)
SetOwnership(mu_Other,False)
Roo_mu_Other_UP = ROOT.RooDataHist("mu_Other_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_Other_UP))
mu_Other_UP = ROOT.RooHistPdf("mu_Other_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_mu_Other_UP)
SetOwnership(mu_Other_UP,False)
Roo_mu_Other_Down = ROOT.RooDataHist("mu_Other_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_mu_Other_Down))
mu_Other_Down = ROOT.RooHistPdf("mu_Other_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_mu_Other_Down)
SetOwnership(mu_Other_Down,False)

Roo_el_DY_S = ROOT.RooDataHist("el_DY_S","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_S))
el_DY_S = ROOT.RooHistPdf("el_DY_S", "", ROOT.RooArgSet(x), Roo_el_DY_S)
SetOwnership(el_DY_S,False)
Roo_el_DY_S_UP = ROOT.RooDataHist("el_DY_S_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_S_UP))
el_DY_S_UP = ROOT.RooHistPdf("el_DY_S_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_el_DY_S_UP)
SetOwnership(el_DY_S_UP,False)
Roo_el_DY_S_Down = ROOT.RooDataHist("el_DY_S_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_S_Down))
el_DY_S_Down = ROOT.RooHistPdf("el_DY_S_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_el_DY_S_Down)
SetOwnership(el_DY_S_UP,False)
Roo_el_DY_B = ROOT.RooDataHist("el_DY_B","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_B))
el_DY_B = ROOT.RooHistPdf("el_DY_B", "", ROOT.RooArgSet(x), Roo_el_DY_B)
SetOwnership(el_DY_B,False)
Roo_el_DY_B_UP = ROOT.RooDataHist("el_DY_B_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_B_UP))
el_DY_B_UP = ROOT.RooHistPdf("el_DY_B_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_el_DY_B_UP)
SetOwnership(el_DY_B_UP,False)
Roo_el_DY_B_Down = ROOT.RooDataHist("el_DY_B_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_DY_B_Down))
el_DY_B_Down = ROOT.RooHistPdf("el_DY_B_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_el_DY_B_Down)
SetOwnership(el_DY_B_Down,False)
Roo_el_Other = ROOT.RooDataHist("el_Other","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_Other))
el_Other = ROOT.RooHistPdf("el_Other", "", ROOT.RooArgSet(x), Roo_el_Other)
SetOwnership(el_Other,False)
Roo_el_Other_UP = ROOT.RooDataHist("el_Other_Up","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_Other_UP))
el_Other_UP = ROOT.RooHistPdf("el_Other_muMassScaleUp", "", ROOT.RooArgSet(x), Roo_el_Other_UP)
SetOwnership(el_Other_UP,False)
Roo_el_Other_Down = ROOT.RooDataHist("el_Other_Down","", ROOT.RooArgList(x), ROOT.RooFit.Import(h_el_Other_Down))
el_Other_Down = ROOT.RooHistPdf("el_Other_muMassScaleDown", "", ROOT.RooArgSet(x), Roo_el_Other_Down)
SetOwnership(el_Other_Down,False)

year="2018"
cg="bb"

flavor="mu"
files=data_files
if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
else: files = [file_ for file_ in files if 'ele' in file_]
if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
else:                 files=[file_ for file_ in files if '_2018' in file_]
if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

datafile=files[0]
eventList=[]
f=open("dataList/"+datafile,"r")
for m in f:

    m=float(m)
    eventList.append(m)

f.close()
m_mu = ROOT.RooRealVar("mass_mu","mass_mu",0 ,3500)
SetOwnership(m_mu, False)
m_mu_arg = ROOT.RooArgSet(m_mu, "mass_mu")
SetOwnership(m_mu_arg, False)
mu_data_obs=ROOT.RooDataSet("mu_data_obs", "mu_data_obs", m_mu_arg)
SetOwnership(mu_data_obs, False)
for mass in eventList:
    m_mu=mass
    mu_data_obs.add(m_mu_arg, 1.0)

print(mu_data_obs.sumEntries()) 
#fil=ROOT.TFile.Open("templates/testWS.root", "RECREATE")
#mu_data_obs.write()
#fil.Save()
#print(m_mu_arg.GetName())




flavor="el"
files=data_files
if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
else: files = [file_ for file_ in files if 'ele' in file_]
if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
else:                 files=[file_ for file_ in files if '_2018' in file_]
if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

datafile=files[0]
eventList=[]
f=open("dataList/"+datafile,"r")
for m in f:

    m=float(m)
    eventList.append(m)
f.close()
m_el = ROOT.RooRealVar("mass_el","mass_el",0 ,3500)
SetOwnership(m_el, False)
m_el_arg = ROOT.RooArgSet(m_el, "mass_el")
SetOwnership(m_el_arg, False)
el_data_obs=ROOT.RooDataSet("el_data_obs", "el_data_obs", m_el_arg)
SetOwnership(el_data_obs, False)
for mass in eventList:
    #print (mass)
    m_el=mass
    el_data_obs.add(m_el_arg, 1.0)

print(el_data_obs.sumEntries())

ws=ROOT.RooWorkspace("w")
ws.Import(el_data_obs) 
ws.Import(mu_data_obs)
ws.Import(mu_DY_S)
ws.Import(mu_DY_S_UP)
ws.Import(mu_DY_S_Down)
ws.Import(mu_DY_B)
ws.Import(mu_DY_B_UP)
ws.Import(mu_DY_B_Down)
ws.Import(mu_Other)
ws.Import(mu_Other_UP)
ws.Import(mu_Other_Down)
ws.Import(el_DY_S)
ws.Import(el_DY_S_UP)
ws.Import(el_DY_S_Down)
ws.Import(el_DY_B)
ws.Import(el_DY_B_UP)
ws.Import(el_DY_B_Down)
ws.Import(el_Other)
ws.Import(el_Other_UP)
ws.Import(el_Other_Down)
ws.writeToFile("testRooFit.root")








