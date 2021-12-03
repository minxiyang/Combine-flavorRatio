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
    massCut=1000
    print("test run with mass cutoff "+str(massCut))
    for year in ["2016", "2017", "2018", "Run3"]:
        #for cg in ["bb","be"]:
        if year == "Run3": 
            scale="Run3"
        else:
            scale="Run2"
        for cg in ["bb","be"]:
            cardName="ch"+year+cg+"_"+str(massCut)+"cut"
            tmpName="tmp"+year+cg+"_"+str(massCut)+"cut"
            fileName="output"+year+cg+"_"+str(massCut)+"cut"
            plotName="nll"+year+cg+"_"+str(massCut)+"cut"
            cardNames.append(cardName)
            acc_eff = getAccEffAndErr(year, cg, massCut)
            if scale=="Run3":
                tmps=tmpHandle("2018", cg, scale=scale)
            else:
                tmps=tmpHandle(year, cg, scale=scale)
            tmps.createTmps(massCut, sys_uncers)

            tmps.saveTmps(tmpName)
            if scale == "Run3":
                plotTmps("Run3", cg, massCut, tmps.templates)
                writeDatacards(cardName, tmpName, "Run3", cg, tmps.templates, acc_eff)
                runCB(scanRange, fileName, 0, cardName)
                inputs={"result":fileName}
                plotNll('Run3', cg, massCut, False, "Run3", 0, **inputs)
                impactOut="Impact_cut"+str(massCut)+"_"+year+"_"+cg
                #plotImpact(cardName, impactOut)
                #plotImpact(cardName, impactOut, False)
            
            
    runCB(scanRange, "Run3and2Combine_cut"+str(massCut), 0, *cardNames)
    inputs={"result":"Run3and2Combine_cut"+str(massCut)}
    plotNll("Run3and2", "all", massCut, False, "Combine",  0, **inputs)
    #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut))
    #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut), False)
        

if __name__=="__main__":
    main()
