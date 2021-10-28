import ROOT
from Parameters import *
import glob



def fileList(process, flavor, year):


    if flavor in "el": flavor_name="electrons"
    else: flavor_name="muons"

    files=glob.glob("crabOutputs/"+process+"/*"+flavor_name+"*root")
    file_list=[]

    for file_ in files:

        file_=file_.split("/")[-1]
        file_=file_.strip(".root")

        if "2018" in file_: yr="2018"
        elif "2016" in file_: yr="2016"
        else: yr="2017"
        if yr not in year: continue

        file_list.append(file_)
   
    return file_list




def hist2Load(process, flavor, year):

    if flavor == "el":

        load_dir="ElectronSelectionElectronsAllSignsHistos"
        uncertainties=["PUScaleUp", "PUScaleDown", "PrefireUp", "PrefireDown", "ScaleUp", "ScaleDown"]
        if process=="DY": hist_name="DielectronResponse"
        else: hist_name="DielectronMass"

    else:    

       load_dir="Our"+year+"MuonsPlusMuonsMinusHistos"
       uncertainties=["Smear", "ScaleUp", "ScaleDown", "MuonID"]
       if process=="DY": hist_name="DimuonResponse"
       else: hist_name="DimuonMassVertexConstrained"

    hist_pair_list=[]
   
    if "Response" in hist_name:
        for cg in ['_bb', '_be']:
            hist_pair_list.append((load_dir+"/"+hist_name+cg, hist_name+cg))
            for uncert in uncertainties: 
                if uncert=="ScaleUp" or uncert=="ScaleDown":
                    hist1=load_dir+"/"+hist_name+"Mass"+uncert+cg
                    hist_pair_list.append((hist1, hist_name+cg+"_Mass"+uncert))
                #elif uncert=="Smear":
                else:
                    hist1=load_dir+"/"+hist_name+uncert+cg
                    hist_pair_list.append((hist1, hist_name+cg+"_"+uncert))
    else:

        for cg in ['_bb', '_be']:
            hist_pair_list.append((load_dir+"/"+hist_name+cg, hist_name+cg))
            for uncert in uncertainties:
                if uncert=="ScaleUp" or uncert=="ScaleDown":
                    hist1=load_dir+"/"+hist_name+uncert+cg
                    hist_pair_list.append((hist1, hist_name+cg+"_Mass"+uncert))
                else:
                    hist1=load_dir+"/"+hist_name+uncert+cg
                    hist_pair_list.append((hist1, hist_name+cg+"_"+uncert))
  
    return hist_pair_list

def fineBinJet(hFine ,hJet):
    j=0
    for i in range(hFine.GetNbinsX()):
        #for j in range(hJet.GetNbinsX()):    
        cent=hFine.GetBinCenter(i)
        if cent>=hJet.GetBinLowEdge(j) and cent<hJet.GetBinLowEdge(j+1): 
            val=hJet.GetBinContent(j)
            #err=hJet.GetBinError(j)
            hFine.SetBinContent(i, val)
            #hFine.SetBinError(i, err)
        else:
            j+=1
def preprocess():
    for process in ["Other","DY"]:
        for flavor in ["mu","el"]:
            for year in ["2016","2017","2018"]:
                print("start merge the data for %s MC in %s channel at %s year" %(process, flavor, year))
                hist_dict={}
                if process == "Other":
                    hist_dict["Jets_"+year+"_"+flavor+"_bb"]=ROOT.TH1D("Jets_"+year+"_"+flavor+"_bb", " ", 20000 ,0. ,20000.)
                    hist_dict["Jets_"+year+"_"+flavor+"_be"]=ROOT.TH1D("Jets_"+year+"_"+flavor+"_be", " ", 20000 ,0. ,20000.)
                    if flavor == "mu":
                        if year=="2016":
                            rootFile=ROOT.TFile.Open("crabOutputs/Jets/jets_muons_2016.root")
                            hbb=rootFile.Get("jetsBB")
                            hbb.SetDirectory(0)
                            fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_bb"], hbb)
                            hbe=rootFile.Get("jetsBE")
                            hbe.SetDirectory(0)
                            fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_be"], hbe)
                            rootFile.Close()
                        else:
                            if year=="2018": scaleF=0.5885366
                            else: scaleF=0.4114634
                            rootFile=ROOT.TFile.Open("crabOutputs/Jets/combined_jet_log_BB_"+year+"_binWidth.root")
                            hbb=rootFile.Get("DATA_mass_log_BB")
                            hbb.SetDirectory(0)
                            hbb.Scale(scaleF)
                            fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_bb"], hbb)
                            rootFile.Close()
                            rootFile=ROOT.TFile.Open("crabOutputs/Jets/combined_jet_log_BE_"+year+"_binWidth.root")
                            hbe=rootFile.Get("DATA_mass_log_BE")
                            hbe.SetDirectory(0)
                            hbe.Scale(scaleF)
                            fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_be"], hbe)
                            rootFile.Close()

                    else:
                        rootFile=ROOT.TFile.Open("crabOutputs/Jets/Result_"+year+".root")
                        hbb=rootFile.Get("jets_h_mee_all_BB")
                        hbb.SetDirectory(0)
                        fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_bb"], hbb)
                        hbe=rootFile.Get("jets_h_mee_all_BE")
                        hbe.SetDirectory(0)
                        fineBinJet(hist_dict["Jets_"+year+"_"+flavor+"_be"], hbe)
                        rootFile.Close()

                
                files=fileList(process, flavor, year)
                hist_pairs=hist2Load(process, flavor, year)
                if flavor == "el": lumi=lumi_el[year]
                else: lumi=lumi_mu[year]
                if year=="2016": zFacs=zScale2016.copy()
                elif year=="2018": zFacs=zScale2018.copy()
                else: zFacs=zScale.copy()
                if flavor == "el": zFac=zFacs["electrons"]
                else: zFac=zFacs["muons"]

                #hist_dict={}

                for pair in hist_pairs:
                    if "Response" in pair[0]: hist_dict[pair[1]]=ROOT.TH2D(pair[1],pair[1],3500, 0., 3500., 350, 0., 3500.)
                    else: hist_dict[pair[1]]=ROOT.TH1D(pair[1], pair[1], 20000 ,0. ,20000.) 
                    if process == "Other":
                            if 'bb' in pair[0]:  hist_dict[pair[1]].Add(hist_dict["Jets_"+year+"_"+flavor+"_bb"])
                            if 'be' in pair[0]:  hist_dict[pair[1]].Add(hist_dict["Jets_"+year+"_"+flavor+"_be"])

                             
                for file_ in files:
           
                    key=file_.split('_')
                    if key[-1] in "ext": 
                        key=key[-2]+"_ext"
                        file_=file_+"t"
                    else: key=key[-1]
                    if year not in "2017": key=key+"_"+year
                    if "ttbar" in file_: 
                        if "lep" not in key: key="ttbar_lep_"+key
                        else: key="ttbar_"+key
               
                    
                    if key in crossSections.keys(): xsec=crossSections[key] 
                    else: continue
                    #print(file_)
                    rootFile=ROOT.TFile.Open("crabOutputs/"+process+"/"+file_+".root")
                    neg=rootFile.FindObjectAny("weights").GetBinContent(1)/(rootFile.FindObjectAny("weights").GetBinContent(1)+rootFile.FindObjectAny("weights").GetBinContent(2)) 
                    nev=rootFile.FindObjectAny("Events").GetBinContent(1)
                    for pair in hist_pairs:
                        #print(pair)
                        temphist=rootFile.Get(pair[0])
                        temphist.SetDirectory(0)
                        #if process == "Other":
                        #    if 'bb' in pair[0]:  hist_dict[pair[1]].Add(hist_dict["Jets_"+year+"_"+flavor+"_bb"])
                        #    if 'be' in pair[0]:  hist_dict[pair[1]].Add(hist_dict["Jets_"+year+"_"+flavor+"_be"])
                        if flavor == "mu":
                            hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac)
                        elif 'bb' in pair[0]:
                            hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac[1])
                        else:
                            hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac[2])
                    rootFile.Close()
               
                f=ROOT.TFile.Open("MC/"+process+"_"+flavor+"_"+year+".root","RECREATE")
       
                for key in hist_dict.keys():hist_dict[key].Write()
             
                f.Save()
                f.Close()






