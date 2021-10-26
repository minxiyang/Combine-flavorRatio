import ROOT
import root_numpy
import numpy as np

def getFrAndLimits(rootFile):

    f=ROOT.TFile.Open("combineOutputs/"+rootFile+".root","r")
    tree=f.Get("limit")
    nll=root_numpy.tree2array(tree,"deltaNLL")
    r=root_numpy.tree2array(tree,"r")
   
    idx=np.argmin(nll)
    r_min=r[idx]
    r1=r2=r3=r4=0
 
    for i in range(1,min(len(r)-idx, idx)):
        #print(nll[idx-i])
        if nll[idx-i]<1:r1=r[idx-i] 
        elif nll[idx-i]<4: r3=r[idx-i]
        if nll[idx+i]<1: r2=r[idx+i]
        elif nll[idx+i]<4: r4=r[idx+i]
        
     
    f.Close()
    if r3==0 or r4==0: 
        print nll[idx]
        print nll[idx+1]
        print nll[idx-1]
    return [r3, r1, r_min, r2, r4]
   

