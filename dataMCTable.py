import ROOT
from Parameters import data_files

Bins=[400, 600, 900, 1300, 1800, -1]
ranges=[400, 600, 900, 1300, 1800, 6000]
for year in ["2016", "2017", "2018"]:
    for flavor in ["mu", "el"]:
        for cg in ["bb", "be"]:   
            if flavor=="mu": prefix="Dimuon"
            else: prefix="Dielectron"
            DY_f=ROOT.TFile.Open("MC/DY_"+flavor+"_"+year+".root")
            DYM=DY_f.Get(prefix+"Response_"+cg)
            print(prefix+"Response_"+cg)
            DYM.SetDirectory(0)
            DY=DYM.ProjectionX("DY")
            DY.SetDirectory(0)
            DY_f.Close()
       
            Other_f=ROOT.TFile.Open("MC/Other_"+flavor+"_"+year+".root")
            if flavor=="mu": prefix="DimuonMassVertexConstrained"
            else: prefix="DielectronMass"
            Other=Other_f.Get(prefix+"_"+cg)
            Other.SetDirectory(0)
      

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
            dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', 20000, 0, 20000)
            for mass in data: dataHist.Fill(mass) 
            
            yieldText=open("txtResults/"+year+flavor+cg+".txt", "w")
            yieldText.writelines("Range        data        DY        Other \n") 
            for i in range(len(Bins)-1):
                low=Bins[i]
                high=Bins[i+1]
                nevData=dataHist.Integral(low+1, high)
                nevDY=DY.Integral(low+1, high)
                nevOther=Other.Integral(low+1, high)
                line="%s to %s    %s    %s    %s \n"%(str(ranges[i]), str(ranges[i+1]), str(nevData), str(nevDY), str(nevOther))
                yieldText.writelines(line)
            yieldText.close()
             


