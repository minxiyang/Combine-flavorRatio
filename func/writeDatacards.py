from Parameters import eff_corr

def writeDatacards(cardName, fileName, year, cg, templates, acc_eff):

    print('write datacard for %s %s'%(year, cg))

    tmpcard=open("datacards/tmp/card_tmp.txt", "r") 
    tmptxt=tmpcard.read()
    tmptxt=tmptxt.replace('tmp', fileName)
    nev_mu_obs=templates['mu_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_mu_obs',str(nev_mu_obs))
    nev_el_obs=templates['el_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_el_obs',str(nev_el_obs))
    nev_el_dy_s=templates['el_DY_S'].Integral()
    tmptxt=tmptxt.replace('nev_el_dy_s',str(nev_el_dy_s))
    nev_mu_dy_s=templates['mu_DY_S'].Integral()
    tmptxt=tmptxt.replace('nev_mu_dy_s',str(nev_mu_dy_s))
    nev_el_dy_b=templates['el_DY_B'].Integral()
    tmptxt=tmptxt.replace('nev_el_dy_b',str(nev_el_dy_b))
    nev_mu_dy_b=templates['mu_DY_B'].Integral()
    tmptxt=tmptxt.replace('nev_mu_dy_b',str(nev_mu_dy_b))
    nev_el_o=templates['el_Other'].Integral()
    tmptxt=tmptxt.replace('nev_el_o',str(nev_el_o))
    nev_mu_o=templates['mu_Other'].Integral()
    tmptxt=tmptxt.replace('nev_mu_o',str(nev_mu_o))    
    tmptxt=tmptxt.replace('acc_eff_med',str(acc_eff[0]))
    tmptxt=tmptxt.replace('acc_eff_low',str(acc_eff[1]))
    tmptxt=tmptxt.replace('acc_eff_high',str(acc_eff[2]))
    Effv=eff_corr["eff"+cg]
    tmptxt=tmptxt.replace('Effv',Effv)
    trigkey="trig"+year+cg
    Trigv=eff_corr[trigkey]
    tmptxt=tmptxt.replace('trig',trigkey)
    tmptxt=tmptxt.replace('Trigv',Trigv)
    tmptxt=tmptxt.replace('R1','R'+year+cg)
    for uncer in ["muMassScale","elMassScale","Smear","Prefire","PUScale","MuonID"]:
        for key in templates.keys():
            
            if "Down" in key and uncer in key.split("_")[-1] and "S" not in key.split("_")[-2] and "B" not in key.split("_")[-2] and "Other" not in key.split("_")[-2]: 
                key1=key.strip("Down")
                tmptxt=tmptxt.replace(uncer, key1.split("_")[-2]+"_"+uncer)
                break   
    datacard=open("datacards/"+cardName+".txt", "w")  
    datacard.write(tmptxt)
    tmpcard.close()
    datacard.close()

