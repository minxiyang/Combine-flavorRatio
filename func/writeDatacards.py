from Parameters import eff_corr, post_fit_nev

def writeDatacards(cardName, fileName, year, cg, templates, acc_eff, isFold=False):

    print('write datacard for %s %s'%(year, cg))
    if "el_DY_BL" in templates.keys():
        tmpcard=open("datacards/tmp/card_tmp_singleBin.txt", "r")
    if "el_DY_S1" in templates.keys():
        tmpcard=open("datacards/tmp/card_tmp_multiBins.txt", "r")
    elif isFold:
        tmpcard=open("datacards/tmp/card_fold.txt", "r")
    else:
        tmpcard=open("datacards/tmp/card_tmp.txt", "r") 
    tmptxt=tmpcard.read()
    tmptxt=tmptxt.replace('tmp', fileName)
    nev_mu_obs=templates['mu_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_mu_obs',str(nev_mu_obs))
    nev_el_obs=templates['el_data_obs'].Integral()
    tmptxt=tmptxt.replace('nev_el_obs',str(nev_el_obs))
    if nev_el_obs==0: print("yield of dielectron for %s %s is 0"%(cg, year))
    if nev_mu_obs==0: print("yield of dimuon for %s %s is 0"%(cg, year))
   
    if "el_DY_S1" in templates.keys():
        for i in range(10):
            nev_el_dy=templates['el_DY_S'+str(i)].Integral()
            #if cg=="be" and i>0: nev_el_dy1=post_fit_nev[year+cg][i-1]
            nev_el_dy1=nev_el_dy
            #nev_el_dy=templates['el_DY_S'+str(i)].Integral()
            tmptxt=tmptxt.replace('nev_el_dy'+str(i),str(nev_el_dy))
            tmptxt=tmptxt.replace('fev_el_dy'+str(i),str(nev_el_dy1))
            nev_mu_dy=templates['mu_DY_S'+str(i)].Integral()
            tmptxt=tmptxt.replace('nev_mu_dy'+str(i),str(nev_mu_dy))
            if year+cg != "2016bb":
                tmptxt=tmptxt.replace('Rel'+str(i)+'L',str(0.0))
            else:
                tmptxt=tmptxt.replace('Rel'+str(i)+'L',str(0.0))
            tmptxt=tmptxt.replace('Rel'+str(i)+'H',str(10.*nev_el_dy))
    else:
        nev_el_dy_s=templates['el_DY_S'].Integral()
        tmptxt=tmptxt.replace('nev_el_dy_s',str(nev_el_dy_s))
        nev_mu_dy_s=templates['mu_DY_S'].Integral()
        tmptxt=tmptxt.replace('nev_mu_dy_s',str(nev_mu_dy_s))
    if "el_DY_BL" in templates.keys():
        nev_el_dy_bl=templates['el_DY_BL'].Integral()
        tmptxt=tmptxt.replace('nev_el_dy_bl',str(nev_el_dy_bl))
        nev_mu_dy_bl=templates['mu_DY_BL'].Integral()
        tmptxt=tmptxt.replace('nev_mu_dy_bl',str(nev_mu_dy_bl))
        nev_el_dy_bh=templates['el_DY_BH'].Integral()
        tmptxt=tmptxt.replace('nev_el_dy_bh',str(nev_el_dy_bh))
        nev_mu_dy_bh=templates['mu_DY_BH'].Integral()
        tmptxt=tmptxt.replace('nev_mu_dy_bh',str(nev_mu_dy_bh))

    elif not isFold and "el_DY_S1" not in templates.keys():
        nev_el_dy_b=templates['el_DY_B'].Integral()
        tmptxt=tmptxt.replace('nev_el_dy_b',str(nev_el_dy_b))
        nev_mu_dy_b=templates['mu_DY_B'].Integral()
        tmptxt=tmptxt.replace('nev_mu_dy_b',str(nev_mu_dy_b))
    nev_el_o=templates['el_Other'].Integral()
    tmptxt=tmptxt.replace('nev_el_o',str(nev_el_o))
    nev_mu_o=templates['mu_Other'].Integral()
    tmptxt=tmptxt.replace('nev_mu_o',str(nev_mu_o))
    if "el_DY_S1" in templates.keys():
        for i in range(1,10):
            key="S"+str(i)
            tmptxt=tmptxt.replace('acc_eff_med'+str(i),str(acc_eff[key][0]))
            tmptxt=tmptxt.replace('acc_eff_err'+str(i),str(acc_eff[key][1]))
    else:
        tmptxt=tmptxt.replace('acc_eff_med',str(acc_eff[0]))
        tmptxt=tmptxt.replace('acc_eff_err',str(acc_eff[1]))
    Effv=eff_corr["eff"+cg]
    tmptxt=tmptxt.replace('Effv',Effv)
    trigkey="trig"+year+cg
    Trigv=eff_corr[trigkey]
    tmptxt=tmptxt.replace('trig',trigkey)
    tmptxt=tmptxt.replace('Trigv',Trigv)
    if "el_DY_S1" in templates.keys():
        for i in range(1,10):
            tmptxt=tmptxt.replace('R'+str(i),'R'+str(i)+'_'+year+cg)
            tmptxt=tmptxt.replace('Rmu'+str(i),'Rmu'+str(i)+'_'+year+cg)
            tmptxt=tmptxt.replace('Rel'+str(i),'Rel'+str(i)+'_'+year+cg)
            #tmptxt=tmptxt.replace('Rel'+str(i)+'L',)
            #tmptxt=tmptxt.replace('Rel'+str(i)+'H',)
    else:
        tmptxt=tmptxt.replace('R1','R'+year+cg)
        tmptxt=tmptxt.replace('Rmu','Rmu'+year+cg)
        tmptxt=tmptxt.replace('Rel','Rel'+year+cg)
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

