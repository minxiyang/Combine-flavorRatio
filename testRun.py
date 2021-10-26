from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from plotting.plotNll import plotNll
from plotting.plotTmps import plotTmps
from Parameters import sys_uncers 
import os



def main():

    cardNames=[]
    scanRange=(0.7, 1.3)
    massCut=800
    print("test run with mass cutoff "+str(massCut))
    for year in ["2016", "2017", "2018"]:
        for cg in ["bb","be"]:
        
            cardName="ch"+year+cg+"_"+str(massCut)+"cut"
            tmpName="tmp"+year+cg+"_"+str(massCut)+"cut"
            fileName="output"+year+cg+"_"+str(massCut)+"cut"
            plotName="nll"+year+cg+"_"+str(massCut)+"cut"
            cardNames.append(cardName)
            acc_eff = getAccEffAndErr(year, cg, massCut)
            tmps=tmpHandle(year, cg)
            tmps.createTmps(massCut, sys_uncers)

            tmps.saveTmps(tmpName)
            plotTmps(year, cg, massCut, tmps.templates)
            writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff)
            runCB(scanRange, fileName, cardName)
            inputs={"result":fileName}
            plotNll(year, cg, massCut, False, plotName, **inputs)
            
            
    runCB(scanRange, "allYearCombine", *cardNames)
    inputs={"result":"allYearCombine"}
    plotNll("All year", "all category", massCut, False, "allYearCombine", **inputs)
    
        

if __name__=="__main__":
    main()
