import ROOT
import root_numpy
import numpy as np

def getFrAndLimits(rootFile, i=0):

    f=ROOT.TFile.Open("combineOutputs/"+rootFile+".root","r")
    tree=f.Get("limit")
    nll=root_numpy.tree2array(tree,"deltaNLL")
    if i!=0:r=root_numpy.tree2array(tree,"r_bin"+str(i))
    else:r=root_numpy.tree2array(tree,"r")
   
    idx=np.argmin(nll)
    r_min=r[idx]
    r1=r2=r3=r4=0
    #rpre=r[1]
    #ids=np.argsort(nll)
    #nll=np.sort(nll) 
    for i in range(1, len(r)-1):
        
        if nll[i]>1 and nll[i+1]<1:r1=r[i+1] 
        if nll[i]>4 and nll[i+1]<4: r3=r[i+1]
        if nll[i]<1 and nll[i+1]>1: r2=r[i]
        if nll[i]<4 and nll[i+1]>4: r4=r[i]
        
     
    f.Close()
    if r3==0 or r4==0: 
        print nll[idx]
        print nll[idx+1]
        print nll[idx-1]
    return [r3, r1, r_min, r2, r4]
   

