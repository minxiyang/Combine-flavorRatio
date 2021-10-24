import ROOT
from Parameters import data_files, shape_corr
from func.getBngs import getBngs



class tmpHandle(object):

    def __init__(self, year, cg):

         self.year=year
         self.cg=cg
    
    def createTmps(self, massCut, sys_uncers, istoy=False, fr=1.):

        print("create templates for %s %s"%(self.year, self.cg) )
        templates={}
        
        for flavor in ['mu', 'el']:
        
            bng=getBngs(flavor, self.year, self.cg, 400)
            dy_file='DY_'+flavor+'_'+self.year+'.root'

            if flavor=='el':histName_dy='DielectronResponse_'+self.cg
            else: histName_dy="DimuonResponse_"+self.cg

            f_dy=ROOT.TFile.Open("MC/"+dy_file,"r")
            dyHist2D=f_dy.Get(histName_dy)
            dyHist2D.SetDirectory(0)
            dyHist2Dvar={}

            uncers=sys_uncers[flavor]

            for uncer in uncers:
               
                dyHist2Dvar[uncer]=f_dy.Get(histName_dy+'_'+uncer)
                dyHist2Dvar[uncer].SetDirectory(0)

            f_dy.Close()

            other_file='Other_'+flavor+'_'+self.year+'.root'

            if flavor=="el":histName_other='DielectronMass_'+self.cg
            else: histName_other="DimuonMassVertexConstrained_"+self.cg

            f_other=ROOT.TFile.Open("MC/"+other_file,"r")
            otherHist=f_other.Get(histName_other)
            otherHist.SetDirectory(0)
            otherHistvar={}

            for uncer in uncers:
                otherHistvar[uncer]=f_other.Get(histName_other+'_'+uncer)
                otherHistvar[uncer].SetDirectory(0)

            f_other.Close()

            templates[flavor+'_Other']=otherHist.Rebin(len(bng)-1, flavor+'_Other', bng)

            for key in otherHistvar.keys():
 
                
                if "MassScale" in key: key=flavor+key
                
                for corr in shape_corr:
                    key1=key.strip('Up')
                    key2=key1.strip('Down')
                    if key2 in corr and self.cg in corr and self.year in corr: key=corr.split("_")[0]+"_"+key
                if 'Up' in key or 'Down' in key:
                    
                    templates[flavor+'_Other_'+key]=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key, bng)
                else:
                    templates[flavor+'_Other_'+key+'Up']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key+'Up', bng)
                    templates[flavor+'_Other_'+key+'Down']=otherHist.Rebin(len(bng)-1, flavor+'_Other_'+key+'Down', bng)
                
            nBins=int(massCut/10.)
            dy_sig=dyHist2D.ProjectionX("sigx", nBins+1, -1)
            templates[flavor+'_DY_S']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S', bng)
            dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
            templates[flavor+'_DY_B']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B', bng)

            for key in dyHist2Dvar.keys():
            
                keynew=key
                if "MassScale" in key: keynew=flavor+key
                for corr in shape_corr:
                    key1=keynew.strip('Up')
                    key2=key1.strip('Down')
                  
                    if key2 in corr and self.cg in corr and self.year in corr: keynew=corr.split("_")[0]+"_"+keynew

                if 'Up' in key or 'Down' in key:
             
                    dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                    templates[flavor+'_DY_S_'+keynew]=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew, bng)
                    dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
                    templates[flavor+'_DY_B_'+keynew]=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew, bng)

                else:
 
                    dy_sig=dyHist2Dvar[key].ProjectionX("sigx", nBins+1, -1)
                    templates[flavor+'_DY_S_'+keynew+'Up']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Up', bng)
                    templates[flavor+'_DY_S_'+keynew+'Down']=dy_sig.Rebin(len(bng)-1, flavor+'_DY_S_'+keynew+'Down', bng)
                    dy_bkg=dyHist2D.ProjectionX("bkgx", 0, nBins)
                    templates[flavor+'_DY_B_'+keynew+'Up']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew+'Up', bng)
                    templates[flavor+'_DY_B_'+keynew+'Down']=dy_bkg.Rebin(len(bng)-1, flavor+'_DY_B_'+keynew+'Down', bng)

            if not istoy:

                files=data_files

                if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
                else: files = [file_ for file_ in files if 'ele' in file_]

                if self.year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
                elif self.year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
                else:                 files=[file_ for file_ in files if '_2018' in file_]

                if self.cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
                else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

                datafile=files[0]
                data=[]
                f=open("dataList/"+datafile,"r")
                for m in f:

                    m=float(m)
                    data.append(m)
                f.close()
                dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)
                for mass in data: dataHist.Fill(mass)

            else:

                dataHist=ROOT.TH1D(flavor+'_data_obs', flavor+'_data_obs', len(bng)-1,bng)
                dataHist.Add(templates[flavor+'_DY_B'])
                dataHist.Add(templates[flavor+'_Other'])
                if flavor=="mu": dataHist.Add(templates[flavor+'_DY_S'], fr)
                else: dataHist.Add(templates[flavor+'_DY_S'])

            templates[flavor+'_data_obs']=dataHist.Clone()

        self.templates=templates

    def saveTmps(self, tmpName):

        print('save templates for %s %s'%(self.year, self.cg))

        nev_el_dy_s=self.templates['el_DY_S'].Integral()
        nev_mu_dy_s=self.templates['mu_DY_S'].Integral()

        for key in self.templates.keys():
            if 'mu_DY_S' in key: self.templates[key].Scale(nev_el_dy_s/nev_mu_dy_s)

        tempFiles=ROOT.TFile.Open("templates/"+tmpName+".root","RECREATE")
        for key in self.templates.keys(): self.templates[key].Write()
        tempFiles.Save()
        tempFiles.Close()

    def loadTmps(self, tmpName, sys_uncers):

        print('load templates '+tmpName)
        
        templates={}
        tmpFile=ROOT.TFile.Open("templates/"+tmpName+".root","r")
 
        for flavor in ["mu", "el"]:
            templates[flavor+"_data_obs"]=tmpFile.Get(flavor+"_data_obs")
            templates[flavor+"_data_obs"].SetDirectory(0)
            for process in ["DY_S", "DY_B", "Other"]:
                templates[flavor+"_"+process]=tmpFile.Get(flavor+"_"+process)
                templates[flavor+"_"+process].SetDirectory(0)
                for uncer in sys_uncers[flavor]:
                    if "Up" in uncer or "Down" in uncer: templates[flavor+"_"+process+"_"+uncer]=tmpFile.Get(flavor+"_"+process+"_"+flavor+uncer)
                    else: templates[flavor+"_"+process+"_"+uncer]=tmpFile.Get(flavor+"_"+process+"_"+flavor+uncer+"Up") 
                    templates[flavor+"_"+process+"_"+uncer].SetDirectory(0)

        self.templates=templates
