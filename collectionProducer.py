import ROOT
from Variables import *
import glob



def fileList(process, flavor, year):


    if flavor in "el": flavor_name="electrons"
    else: flavor_name="muons"

    files=glob.glob(process+"/crab_output/*"+flavor_name+"*root")
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
        for cate in ['_bb', '_be']:
            hist_pair_list.append((load_dir+"/"+hist_name+cate, hist_name+cate))
            for uncert in uncertainties: 
                if uncert=="ScaleUp" or uncert=="ScaleDown":
                    hist1=load_dir+"/"+hist_name+"Mass"+uncert+cate
                    hist_pair_list.append((hist1, hist_name+cate+"_Mass"+uncert))
                elif uncert=="Smear":
                    hist1=load_dir+"/"+hist_name+uncert+cate
                    hist_pair_list.append((hist1, hist_name+cate+"_"+uncert))
    else:

        for cate in ['_bb', '_be']:
            hist_pair_list.append((load_dir+"/"+hist_name+cate, hist_name+cate))
            for uncert in uncertainties:
                if uncert=="ScaleUp" or uncert=="ScaleDown":
                    hist1=load_dir+"/"+hist_name+uncert+cate
                    hist_pair_list.append((hist1, hist_name+cate+"_Mass"+uncert))
                else:
                    hist1=load_dir+"/"+hist_name+uncert+cate
                    hist_pair_list.append((hist1, hist_name+cate+"_"+uncert))
  
    return hist_pair_list



for process in ["Other","DY"]:
    for flavor in ["mu","el"]:
        for year in ["2016","2017","2018"]:

            files=fileList(process, flavor, year)
            hist_pairs=hist2Load(process, flavor, year)
            if flavor == "el": lumi=lumi_el[year]
            else: lumi=lumi_mu[year]
            if year=="2016": zFacs=zScale2016.copy()
            elif year=="2018": zFacs=zScale2018.copy()
            else: zFacs=zScale.copy()
            if flavor == "el": zFac=zFacs["electrons"]
            else: zFac=zFacs["muons"]

            hist_dict={}

            for pair in hist_pairs:
                if "Response" in pair[0]: hist_dict[pair[1]]=ROOT.TH2D(pair[1],pair[1],3500, 0., 3500., 350, 0., 3500.)
                else: hist_dict[pair[1]]=ROOT.TH1D(pair[1], pair[1], 20000 ,0. ,20000.) 

                             
            for file_ in files:
           
                key=file_.split('_')
                if key[-1] in "ext": 
                    key=key[-2]+"_ext"
                    file_=file_+"t"
                #elif key[-1] in year:
                #    if key[-2] in "ext": key=key[-3]+"_"+key[-2]+"_"+key[-1]
                #    else: key=key[-2]+"_"+key[-1]
                else: key=key[-1]
                if year not in "2017": key=key+"_"+year
                if "ttbar" in file_: 
                    if "lep" not in key: key="ttbar_lep_"+key
                    else: key="ttbar_"+key
                #print(key)
                print(file_)
                if key in crossSections.keys(): xsec=crossSections[key] 
                else: continue
                rootFile=ROOT.TFile.Open(process+"/crab_output/"+file_+".root")
                neg=rootFile.FindObjectAny("weights").GetBinContent(1)/(rootFile.FindObjectAny("weights").GetBinContent(1)+rootFile.FindObjectAny("weights").GetBinContent(2)) 
                nev=rootFile.FindObjectAny("Events").GetBinContent(1)
                for pair in hist_pairs:
                   #print(pair[0])
                   #print(file_+".root")
                   temphist=rootFile.Get(pair[0])
                   temphist.SetDirectory(0)
                   if flavor == "mu":
                       hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac)
                   elif 'bb' in pair[0]:
                       hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac[1])
                   else:
                       hist_dict[pair[1]].Add(temphist, lumi*xsec/nev*(1-2*neg)*zFac[2])
                rootFile.Close()

            f=ROOT.TFile.Open("dataCollection/"+process+"_"+flavor+"_"+year+".root","RECREATE")
            #print(hist_dict.keys()) 
            for key in hist_dict.keys():
                #print(key)
                hist_dict[key].Write()
             
            f.Save()
            f.Close()






