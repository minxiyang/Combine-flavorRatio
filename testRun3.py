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
    scanRange=(0.2, 1.8)
    massCut=400
    print("test run with mass cutoff "+str(massCut))
    for year in ["2018"]:
        for cg in ["bb","be"]:
        
            cardName="ch"+"Run3"+cg+"_"+str(massCut)+"cut"
            tmpName="tmp"+"Run3"+cg+"_"+str(massCut)+"cut"
            fileName="output"+"Run3"+cg+"_"+str(massCut)+"cut"
            plotName="nll"+"Run3"+cg+"_"+str(massCut)+"cut"
            cardNames.append(cardName)
            acc_eff = getAccEffAndErr(year, cg, massCut)
            tmps=tmpHandle(year, cg, scale='Run3')
            tmps.createTmps(massCut, sys_uncers)

            tmps.saveTmps(tmpName)
            plotTmps("Run3", cg, massCut, tmps.templates)
            writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff)
            runCB(scanRange, fileName, 0, cardName)
            inputs={"result":fileName}
            plotNll('', cg, massCut, False, "Run3", 0, **inputs)
            impactOut="Impact_cut"+str(massCut)+"_"+year+"_"+cg
            #plotImpact(cardName, impactOut)
            #plotImpact(cardName, impactOut, False)
            
            
    runCB(scanRange, "2018Combine_cut"+str(massCut), 0, *cardNames)
    inputs={"result":"2018Combine_cut"+str(massCut)}
    plotNll("Run3", "all", massCut, False, "Combine",  0, **inputs)
    #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut))
    #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut), False)
        

if __name__=="__main__":
    main()
