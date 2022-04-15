import ROOT
import math
from math import sqrt
from Parameters import DCBp

def getResolution(year, flavor, cg, mass):

    params = DCBp[year+flavor+cg]    
    DCB={}
    for key in ['alphaL','alphaR','nL','nR','sigma','scale']:

        DCB[key]=0
        n=0.
        for param in params[key]:
            DCB[key]+=param*mass**n
            n+=1


    return DCB 
    











