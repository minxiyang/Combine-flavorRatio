import numpy as np

def average(hist):
    for i in range(0, hist.GetNbinsX()+2):
        val=hist.GetBinContent(i)
        err=hist.GetBinError(i)
        wid=hist.GetBinWidth(i)
        val=val/wid
        err=err/wid
        hist.SetBinContent(i,val)
        hist.SetBinError(i,err)

