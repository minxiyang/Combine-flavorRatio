from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from plotting.plotNll import plotNll
from Parameters import sys_uncers 
import os



def main():

    cardNames=[]
    massCut=800
    scanRange=(0.4,1.8)
    frs=[0.5, 0.75, 1.0, 1.25, 1.5]
    print("run with the different inject flavor ratio and mass cutoff "+str(massCut))
    for year in ["2016", "2017", "2018"]:
        for cg in ["bb","be"]:
            acc_eff = getAccEffAndErr(year, cg, massCut)
            inputs={}
            plotName="nll"+year+cg+"_"+str(massCut)+"cut_"+"fr"
            for fr in frs:
                cardName="ch"+year+cg+"_"+str(massCut)+"cut_"+str(fr)+"fr"
                tmpName="tmp"+year+cg+"_"+str(massCut)+"cut_"+str(fr)+"fr"
                fileName="output"+year+cg+"_"+str(massCut)+"cut_"+str(fr)+"fr"
                cardNames.append(cardName)
                tmps=tmpHandle(year, cg)
                tmps.createTmps(massCut, sys_uncers, True, fr)
                tmps.saveTmps(tmpName)
                writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff)
                runCB(scanRange, fileName, cardName)
                key="fr is "+str(fr)
                inputs[key]=fileName
            plotNll(year, cg, massCut, True, plotName, **inputs)
    
    inputs={}        
    for fr in frs:
        cardNamesfr=[cardName for cardName in cardNames if str(fr) in cardName]
     
        fileName="allYearCombine_"+str(fr)+"fr"
        runCB(scanRange, fileName, *cardNamesfr)
        key="fr is "+str(fr)
        inputs[key]=fileName

    plotNll("All year", "all category", massCut, True, "allYearCombineToy", **inputs)
    
        

if __name__=="__main__":
    main()
