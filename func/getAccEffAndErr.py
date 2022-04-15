import ROOT
import numpy as np
from func.Rebin import Rebin
from func.getBngs import getBngs


def getAccEffAndErr(year, cg, massCut, massCutH=0):

    dyHist2D={}
    scale="Run2"
    if year=="Run3": year="2018"
    elif year=="Phase2": 
        year="2018"
        scale="Phase2"
    f_mu=ROOT.TFile.Open("MC/"+"DY_mu_"+year+".root","r")
    dyHist2D["mu"]=f_mu.Get("DimuonResponse_"+cg)
    dyHist2D["mu"].SetDirectory(0)
    f_mu.Close()
    f_el=ROOT.TFile.Open("MC/"+"DY_el_"+year+".root","r")
    dyHist2D["el"]=f_el.Get("DielectronResponse_"+cg)
    dyHist2D["el"].SetDirectory(0)
    f_el.Close()

    nBins=int(massCut/10.)
    if massCutH<=massCut:
        print(nBins)
        dy_mu=dyHist2D["mu"].ProjectionX("mu", nBins+1, -1)
        dy_el=dyHist2D["el"].ProjectionX("el", nBins+1, -1)
    else:
        nBinsL=nBins
        nBinsH=int(massCutH/10.)
        dy_mu=dyHist2D["mu"].ProjectionX("mu", nBinsL+1, nBinsH)
        dy_el=dyHist2D["el"].ProjectionX("el", nBinsL+1, nBinsH)
  
    if scale=="Phase2":
        print(year)
        bng_el=getBngs("el", year, cg, 150)
        bng_mu=getBngs("mu", year, cg, 150)
        dy_mu=Rebin(dy_mu, "dy_mu", "mu", cg, bng_mu, scale="Phase2") 
        dy_el=Rebin(dy_el, "dy_el", "el", cg, bng_el, scale="Phase2")
    err_mu=ROOT.Double(0)
    n_mu=dy_mu.IntegralAndError(0, -1, err_mu)
    err_el=ROOT.Double(0)
    n_el=dy_el.IntegralAndError(0, -1, err_el)
    acc_eff=n_mu/n_el
    err=acc_eff*np.sqrt((err_mu/n_mu)**2+(err_el/n_el)**2)

    return (acc_eff, err)
    
    
