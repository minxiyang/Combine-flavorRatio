from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from plotting.plotNll import plotNll
from plotting.plotTmps import plotTmps
from plotting.plotImpact import plotImpact
from Parameters import sys_uncers 
import os



def main():

    cardNames=[]
    scanRange=(0.3, 3.0)
    massCut=400
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
            #runCB(scanRange, fileName, cardName)
            inputs={"result":fileName}
            #plotNll(year, cg, massCut, False, plotName, **inputs)
            impactOut="Impact_cut"+str(massCut)+"_"+year+"_"+cg
            #plotImpact(cardName, impactOut)
            #plotImpact(cardName, impactOut, False)
            
            
    runCB(scanRange, "allYearCombine_cut"+str(massCut), *cardNames)
    #inputs={"result":"allYearCombine_cut"+str(massCut)}
    #plotNll("All year", "all category", massCut, False, "allYearCombine_cut"+str(massCut), **inputs)
    plotImpact("combinedCard", "allYearCombine_cut"+str(massCut))
    plotImpact("combinedCard", "allYearCombine_cut"+str(massCut), False)
        

if __name__=="__main__":
    main()
