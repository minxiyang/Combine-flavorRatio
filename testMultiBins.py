from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from func.getFrAndLimits import getFrAndLimits
from plotting.plotNll import plotNll
from plotting.plotTmps import plotTmps
from plotting.plotImpact import plotImpact
from Parameters import sys_uncers 
import os
from json import dumps



def main():
    
    #bng=[200, 300, 400,500,690,900,1250,1610, 2000, 3500]
    bng=[2000, 3500]
    scanRange=(0.1, 4.1)
    histdict={}
    histdictup={}
    histdictdown={}
    for i in range(9):
        cardNames_bb=[]
        cardNames_be=[]

        for year in ["2016", "2017", "2018"]:
            for cg in ["bb","be"]:
                key=cg+year
                if key not in histdict.keys():
                    histdict[key]=[]
                    histdictup[key]=[]
                    histdictdown[key]=[]
                cardName="ch"+year+cg+"_bin"+str(bng[i])+"to"+str(bng[i+1])
                tmpName="tmp"+year+cg+"_bin"+str(bng[i])+"to"+str(bng[i+1])
                fileName="output"+year+cg+"_bin"+str(bng[i])+"to"+str(bng[i+1])
                plotName="nll"+year+cg+"_bin"+str(bng[i])+"to"+str(bng[i+1])
                if cg=="bb": cardNames_bb.append(cardName)
                else: cardNames_be.append(cardName)
                acc_eff = getAccEffAndErr(year, cg, bng[i], bng[i+1])
                tmps=tmpHandle(year, cg)
                tmps.createTmps(bng[i], sys_uncers, isFold=False, massCutH=bng[i+1])
             
                tmps.saveTmps(tmpName)
                #plotTmps(year, cg, massCut, tmps.templates)
                writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff, isFold=False)
                runCB(scanRange, fileName, cardName)
                inputs={"result":fileName}
                plotNll(year, cg, str(bng[i])+"to"+str(bng[1]), False, plotName, **inputs)
                frs=getFrAndLimits(fileName)
                histdict[key].append(str(frs[2]))
                histdictup[key].append(str(frs[3]))
                histdictdown[key].append(str(frs[1]))
                #impactOut="Impact_"+year+"_"+cg
                #plotImpact(cardName, impactOut)
                #plotImpact(cardName, impactOut, False)
            
            
        runCB(scanRange, "allYearCombinebb_bin"+str(bng[i])+"to"+str(bng[i+1]), *cardNames_bb)
        inputs={"result":"allYearCombinebb_bin"+str(bng[i])+"to"+str(bng[i+1])}
        plotNll("All year", "bb", str(bng[i])+"to"+str(bng[i+1]), False, "allYearCombinebb_bin"+str(bng[i])+"to"+str(bng[i+1]), **inputs)
        frs=getFrAndLimits("allYearCombinebb_bin"+str(bng[i])+"to"+str(bng[i+1]))
        key="allYearCombinebb"
        if key in histdict.keys():
            histdict[key].append(str(frs[2]))
            histdictdown[key].append(str(frs[1]))
            histdictup[key].append(str(frs[3]))
        else:
            histdict[key]=[str(frs[2])]
            histdictdown[key]=[str(frs[1])]
            histdictup[key]=[str(frs[3])]
        runCB(scanRange, "allYearCombinebe_bin"+str(bng[i])+"to"+str(bng[i+1]), *cardNames_be)
        inputs={"result":"allYearCombinebe_bin"+str(bng[i])+"to"+str(bng[i+1])}
        plotNll("All year", "be", str(bng[i])+"to"+str(bng[i+1]), False, "allYearCombinebe_bin"+str(bng[i])+"to"+str(bng[i+1]), **inputs)
        frs=getFrAndLimits("allYearCombinebe_bin"+str(bng[i])+"to"+str(bng[i+1]))
        key="allYearCombinebe"
        if key in histdict.keys():
            histdict[key].append(str(frs[2]))
            histdictdown[key].append(str(frs[1]))
            histdictup[key].append(str(frs[3]))
        else:
            histdict[key]=[str(frs[2])]
            histdictdown[key]=[str(frs[1])]
            histdictup[key]=[str(frs[3])]

        cardNames=cardNames_bb+cardNames_be
        runCB(scanRange, "allYearCombine_bin"+str(bng[i])+"to"+str(bng[i+1]), *cardNames)
        inputs={"result":"allYearCombine_bin"+str(bng[i])+"to"+str(bng[i+1])}
        plotNll("All year", "all category", str(bng[i])+"to"+str(bng[i+1]), False, "allYearCombine_bin"+str(bng[i])+"to"+str(bng[i+1]), **inputs)
        frs=getFrAndLimits("allYearCombine_bin"+str(bng[i])+"to"+str(bng[i+1]))
        key="allYearCombine"
        if key in histdict.keys():
            histdict[key].append(str(frs[2]))
            histdictdown[key].append(str(frs[1]))
            histdictup[key].append(str(frs[3]))
        else:
            histdict[key]=[str(frs[2])]
            histdictdown[key]=[str(frs[1])]
            histdictup[key]=[str(frs[3])]
        #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut))
        #plotImpact("combinedCard", "allYearCombine_cut"+str(massCut), False)
    print(histdictdown)
    print(histdict) 
    print(histdictup)
    with open("txtResults/BinbyBinFR_fold.txt", "w") as txt:
        txt.write(dumps(histdictdown))
        txt.write(dumps(histdict))
        txt.write(dumps(histdictup))
               

if __name__=="__main__":
    main()
