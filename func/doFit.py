from scipy.optimize import leastsq
from scipy import stats
import ROOT
import numpy as np




def fit_func(p, x, vals, errs):

   a0, a1, a2, a3, a4= p
   y = x**a1 * np.exp(a0 + a2*x + a3*x**2 + a4*x**3)
   res = (vals - y)/errs

   return res

def doFit(fileName, flavor, cg, year):

    fileName = "MC/"+fileName+".root"
    f = ROOT.TFile.Open(fileName, "read")
    if flavor == "mu": prefix="Dimuon"
    else: prefix="Dielectron"

    if "DY" in fileName:
        reM = f.Get(prefix+"Response_"+cg)
        reM.SetDirectory(0)
        f.Close()
        histo = reM.ProjectionY()
        mass = range(405, 3500, 10)
        mass = np.asarray(mass)
    else:
        if flavor == "mu": histo = f.Get(prefix+"MassVertexConstrained_"+cg)
        else: histo = f.Get(prefix+"Mass_"+cg)
        histo.SetDirectory(0)
        f.Close()
        histo.Sumw2()
        #bins = range(400, 901, 100)+ range(1000, 1601, 200) + [2000, 2500, 3500]
        #bins = np.asarray(bins, np.float)
        #print(bins)
        #histo = histo.Rebin(len(bins)-1, "hist", bins)
        histo = histo.Rebin(100)
        mass = []
        #mass = range(450, 1000, 100) + [1100, 1300, 1500, 1800, 2250, 3000]
        #mass = np.asarray(mass)
        #print(histo.GetNbinsX())
        for i in range(5, 36):
            val=histo.GetBinContent(i)
            wid=histo.GetBinWidth(i)
            err=histo.GetBinError(i)
            #print(wid)
            histo.SetBinContent(i, val/wid)
            histo.SetBinError(i, err/wid)
            if val > 0: mass.append(i*100.-50.)
        mass = np.asarray(mass)
    vals=[]
    errs=[]
    if "DY" in fileName:
        for i in range(41, 351):

            vals.append(histo.GetBinContent(i))
            errs.append(histo.GetBinError(i))
        #mass = range(400, 3501, 10)
    else:
        for i in range(5, 36):
            if histo.GetBinContent(i)>0:
                vals.append(histo.GetBinContent(i))
                errs.append(histo.GetBinError(i))
        #mass = range(400, 3001, 100)
        


    vals=np.asarray(vals)
    errs=np.asarray(errs)
    #print(vals)
    #print(errs)
    #print(mass)
    #mass = range(410, 3501, 10)
    #mass  = np.asarray(mass)
    #print(mass[309])
    if "DY" in fileName: para0 = [30., -4.02139968e+00, -3.56502089e-04, -1.24234837e-07, -2.16295719e-11]
    else: para0 = [23, -3, -1e-2, -1e-10, -2.35e-10] 
    #print(fit_func(para0, 500))
    para0 = np.asarray(para0)
    para = leastsq(fit_func, para0, args=(mass, vals, errs))
    res = fit_func(para[0], mass, vals, errs)
    chi2 = sum(res**2)
    dof = len(vals)-5
    pValue= stats.chi2.cdf(chi2, len(vals)-5)
    fitResult={}
    fitResult["pValue"]=pValue
    fitResult["chi2"]=chi2
    fitResult["dof"]=dof
    fitResult["param"]=para[0]
    return fitResult
