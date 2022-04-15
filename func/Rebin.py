import ROOT
from Parameters import Run3_scale, phase2_scale_el, phase2_scale_mu


def Rebin(hist, name, flavor, cg, bngs, scale="Run2", CI=False):
    
    if scale=="Run2":
        for i in range(hist.GetNbinsX()):
            m=hist.GetBinCenter(i)
            val=hist.GetBinContent(i)
            sFac=1.
            if CI and flavor == "el": sFac=sFac*(1.+0.2*(m/2000.)**2)
            hist.SetBinContent(i, val*sFac)
        hist=hist.Rebin(len(bngs)-1, name, bngs)

    elif scale=="Run3": 
       for i in range(hist.GetNbinsX()):
           m=hist.GetBinCenter(i)
           val=hist.GetBinContent(i)
           sFac=Run3_scale[0]+Run3_scale[1]*m+Run3_scale[2]*m**2+Run3_scale[3]*m**3
           if CI and flavor == "el": sFac=sFac*(1.+0.2*(m/2000.)**2)
           hist.SetBinContent(i, val*sFac)
       hist=hist.Rebin(len(bngs)-1, name, bngs)
       hist.Scale(160./60.)

    else:
        if flavor == "el": scaleFs=phase2_scale_el[cg]
        else: scaleFs=phase2_scale_mu[cg]
        for i in range(hist.GetNbinsX()):
            m=hist.GetBinCenter(i)
            val=hist.GetBinContent(i)
            sFac=scaleFs[0]+scaleFs[1]*m+scaleFs[2]*m**2+scaleFs[3]*m**3
            if flavor == "el": 
                if CI:
                    sFac=sFac*(1.+0.2*(m/2000.)**2)
            #print(sFac)
            #sFac=1.0
            hist.SetBinContent(i, val*sFac)
        hist=hist.Rebin(len(bngs)-1, name, bngs)
        if flavor == "mu": hist.Scale(3000./61.)
        else: hist.Scale(3000./59.)
    hist.SetBinContent(-1, 0)
    return hist

   
