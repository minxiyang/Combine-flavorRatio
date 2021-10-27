import ROOT
import numpy as np

def getAccEffAndErr(year, cg, massCut):

    dyHist2D={}
    f_mu=ROOT.TFile.Open("MC/"+"DY_mu_"+year+".root","r")
    dyHist2D["mu"]=f_mu.Get("DimuonResponse_"+cg)
    dyHist2D["mu"].SetDirectory(0)
    f_mu.Close()
    f_el=ROOT.TFile.Open("MC/"+"DY_el_"+year+".root","r")
    dyHist2D["el"]=f_el.Get("DielectronResponse_"+cg)
    dyHist2D["el"].SetDirectory(0)
    f_el.Close()

    nBins=int(massCut/10.)

    dy_mu=dyHist2D["mu"].ProjectionX("mu", nBins+1, -1)
    dy_el=dyHist2D["el"].ProjectionX("el", nBins+1, -1)
    err_mu=ROOT.Double(0)
    n_mu=dy_mu.IntegralAndError(0, -1, err_mu)
    err_el=ROOT.Double(0)
    n_el=dy_el.IntegralAndError(0, -1, err_el)
    acc_eff=n_mu/n_el
    err=acc_eff*np.sqrt((err_mu/n_mu)**2+(err_el/n_el)**2)

    return (acc_eff, err)
    
    
