from Parameters import eff_corr, post_fit_nev, def_bng
import ROOT
import math
from func.getAccEffAndErr import getAccEffAndErr



def writeDatacards_unbinned(cardName, year, cg, massCut):

    for flavor in ["mu", "el"]:
        for process in ["DY", "Other"]:

            name=process+"_"+flavor+"_"+year
            fileName = "MC/"+name+".root"
            f = ROOT.TFile.Open(fileName, "read")
            
            if flavor == "mu":
                if process == "Other":
                    histName = "DimuonMassVertexConstrained_"+cg
                    histo_other = f.Get(histName)
                    for i in range(0, 150): 
                        histo_other.SetBinContent(i, 0)
                    nev_mu_o = str(histo_other.Integral(151, -1))
                else:
                    MName = "DimuonResponse_"+cg
                    M = f.Get(MName)
                    histo_b = M.ProjectionX("hmu", 15, massCut/10)
                    nev_mu_dy_b = str(histo_b.Integral(151, -1))
            else:
                if process == "Other":
                    histName = "DielectronMass_"+cg
                    histo_other = f.Get(histName)
                    for i in range(0, 150): 
                        histo_other.SetBinContent(i, 0)
                    nev_el_o = str(histo_other.Integral(151, -1))
                else:
                    MName = "DielectronResponse_"+cg
                    M = f.Get(MName)
                    histo_b = M.ProjectionX("hel1", 15, massCut/10)
                    histo_s = M.ProjectionX("hel2", massCut/10+1, -1)
                    nev_el_dy_s = str(histo_s.Integral(151, -1))
                    nev_el_dy_b = str(histo_b.Integral(151, -1))
             
            f.Close()
    print((nev_el_o, nev_el_dy_b, nev_el_dy_s, nev_mu_o, nev_mu_dy_b))
    
    mutmp = "mu"+cg+year
    eltmp = "el"+cg+year
    cg_up = cg+"_scaleUp"
    cg_down = cg+"_scaleDown"
    cg_smear = cg+"_smear"
    cg_ID = cg+"_ID"
    cg_puup = cg+"_puup"
    cg_pudown = cg+"_pudown"
    cg_preup = cg+"_preup"
    cg_predown = cg+"_predown" 
    cut = str(massCut)
    tmpcard=open("datacards/tmp/card_tmp_unbinned.txt", "r") 
    tmptxt=tmpcard.read()
    tmptxt=tmptxt.replace('nev_mu_dy_b', nev_mu_dy_b)
    tmptxt=tmptxt.replace('nev_mu_o', nev_mu_o)
    tmptxt=tmptxt.replace('nev_el_dy_b', nev_el_dy_b)
    tmptxt=tmptxt.replace('nev_el_dy_s', nev_el_dy_s)
    tmptxt=tmptxt.replace('nev_el_o', nev_el_o)
    tmptxt=tmptxt.replace('mutmp', mutmp)
    tmptxt=tmptxt.replace('eltmp', eltmp)
    tmptxt=tmptxt.replace('cut', cut)
    trigkey="trig"+year+cg
    Trigv=eff_corr[trigkey]
    # year_flavor_cg 
    if year == "2016" or cg == "be":
        tmptxt=tmptxt.replace('IDvar', "mu_"+year+"_"+cg+"_IDvar")
    tmptxt=tmptxt.replace('el_massvar',"el_"+year+"_"+cg+"_massvar")
    if year == "2016":
        tmptxt=tmptxt.replace('mu_massvar',"mu_"+year+"_"+cg+"_massvar")
    else:
        tmptxt=tmptxt.replace('mu_massvar',"massvar")             
    tmptxt=tmptxt.replace('trig', 'trig'+year+cg)
    #tmptxt=tmptxt.replace('ID', 'ID'+year+cg)
    if cg == "bb": 
        tmptxt=tmptxt.replace('Effv', '1.06')
    else: 
        tmptxt=tmptxt.replace('Effv', '1.08')
    tmptxt=tmptxt.replace('Trigv',Trigv)
    acc_eff = getAccEffAndErr(year, cg, massCut)
    tmptxt=tmptxt.replace('acc_eff_med',str(acc_eff[0]))
    tmptxt=tmptxt.replace('acc_eff_err',str(acc_eff[1])) 
    tmptxt=tmptxt.replace('R1','R'+year+cg)
    tmptxt=tmptxt.replace('Rmu','Rmu'+year+cg)
    tmptxt=tmptxt.replace('Rel','Rel'+year+cg)
    txts = []
    for i in range(5):
        tmptxt_rand = tmptxt.replace('mucg',cg+"_rand"+str(i))
        tmptxt_rand = tmptxt_rand.replace('elcg',cg+"_rand"+str(i)) 
        datacard=open("datacards/"+cardName+"_rand"+str(i)+".txt", "w")  
        datacard.write(tmptxt_rand)
        datacard.close()
    tmptxt=tmptxt.replace('mucg',cg)
    tmptxt=tmptxt.replace('elcg',cg)
    datacard=open("datacards/"+cardName+".txt", "w")  
    datacard.write(tmptxt)
    datacard.close()

    #tmptxt_up=tmptxt.replace('elcg',cg_up)
    #tmptxt_up=tmptxt_up.replace('mucg',cg_down)
    #tmptxt_down=tmptxt.replace('mucg',cg_up)
    #tmptxt_down=tmptxt_down.replace('elcg',cg_down)
    #tmptxt_muup=tmptxt.replace('mucg',cg_up)
    #tmptxt_muup=tmptxt_muup.replace('elcg',cg)
    #tmptxt_mudown=tmptxt.replace('mucg',cg_down)
    #tmptxt_mudown=tmptxt_mudown.replace('elcg',cg)
    #tmptxt_ID=tmptxt.replace('mucg',cg_ID)
    #tmptxt_ID=tmptxt_ID.replace('elcg',cg)
    #tmptxt_smear=tmptxt.replace('mucg',cg_smear)
    #tmptxt_smear=tmptxt_smear.replace('elcg',cg)
    #tmptxt_elup=tmptxt.replace('elcg',cg_up)
    #tmptxt_elup=tmptxt_elup.replace('mucg',cg)
    #tmptxt_eldown=tmptxt.replace('elcg',cg_down)
    #tmptxt_eldown=tmptxt_eldown.replace('mucg',cg)
    #tmptxt_puup=tmptxt.replace('elcg',cg_puup)
    #tmptxt_pudown=tmptxt.replace('elcg',cg_pudown)
    #tmptxt_puup=tmptxt_puup.replace('mucg',cg)
    #tmptxt_pudown=tmptxt_pudown.replace('mucg',cg)
    #tmptxt_preup=tmptxt.replace('elcg',cg_preup)
    #tmptxt_predown=tmptxt.replace('elcg',cg_predown)
    #tmptxt_preup=tmptxt_preup.replace('mucg',cg)
    #tmptxt_predown=tmptxt_predown.replace('mucg',cg)
    #file_dict = [(tmptxt_center, cardName), (tmptxt_muup, cardName+"_muup"), (tmptxt_mudown, cardName+"_mudown"), (tmptxt_elup, cardName+"_elup"), (tmptxt_eldown, cardName+"_eldown"), (tmptxt_smear, cardName+"_smear"), (tmptxt_ID, cardName+"_ID"), (tmptxt_puup, cardName+"_puup"), (tmptxt_pudown, cardName+"_pudown"), (tmptxt_preup, cardName+"_preup"), (tmptxt_predown, cardName+"_predown")]
    #tmptxt_up=tmptxt.replace('mucg',cg_up)
    #tmptxt_down=tmptxt.replace('mucg',cg_down)
    #tmptxt_up_up=tmptxt_up.replace('elcg',cg_up)
    #tmptxt_up_down=tmptxt_up.replace('elcg',cg_down)
    #tmptxt_down_up=tmptxt_down.replace('elcg',cg_up)
    #tmptxt_down_down=tmptxt_down.replace('elcg',cg_down)
    #file_dict = [(tmptxt_center, cardName), (tmptxt_up_up, cardName+"_muup_elup"), (tmptxt_up_down, cardName+"_muup_eldown"), (tmptxt_down_up, cardName+"_mudown_elup"), (tmptxt_down_down, cardName+"_mudown_eldown")] 
    #for txtfs in file_dict:
        #datacard=open("datacards/"+txtfs[1]+".txt", "w")  
        #datacard.write(txtfs[0])
        #datacard.close()

    tmpcard.close()

