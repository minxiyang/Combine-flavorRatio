import ROOT
from Parameters import Run3_scale, phase2_scale_el, phase2_scale_mu


def Rebin(hist, name, flavor, cg, bngs, scale="Run2"):

    if scale=="Run2":
        hist=hist.Rebin(len(bngs)-1, name, bngs)

    elif scale=="Run3": 
       for i in range(hist.GetNbinsX()):
           m=hist.GetBinCenter(i)
           val=hist.GetBinContent(i)
           sFac=Run3_scale[0]+Run3_scale[1]*m+Run3_scale[2]*m**2+Run3_scale[3]*m**3
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
            hist.SetBinContent(i, val*sFac)
        hist=hist.Rebin(len(bngs)-1, name, bngs)
        hist.Scale(50.)
    return hist

   
