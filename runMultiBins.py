from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from plotting.plotNll import plotNll
from plotting.plotTmps import plotTmps
from plotting.plotImpact import plotImpact
from Parameters import sys_uncers
from func.getFrAndLimits import getFrAndLimits
from func.writeTxt import writeTxt 
import os


#--floatOtherPOIs=1
def main():

    cardNames=[]
    cardNames_bb=[]
    cardNames_be=[]
    scanRange=(0, 3.)
    Bngs=[200,300,400,500,690,900,1250,1610,2000,3500]
    FRmed={} 
    FRlow={}
    FRhigh={}
    #print("test run with mass cutoff "+str(massCut))
    for year in ["2016","2017","2018"]:
        for cg in ["bb","be"]:
            key=year+cg
            FRmed[key]=[]
            FRlow[key]=[]
            FRhigh[key]=[]
            cardName="ch"+year+cg+"_"+"multiBins"
            tmpName="tmp"+year+cg+"_"+"multiBins"
            #fileName="output"+year+cg+"_"+str(massCut)+"cut"
            fileName=year+cg+"_MultiBins"
            plotName="MultiBins"
            cardNames.append(cardName)
            if cg=="bb":cardNames_bb.append(cardName)
            else: cardNames_be.append(cardName)
            Bngs1=Bngs+[-1]
            acc_eff={}
            for i in range(1, 11):
                acc_eff['S'+str(i)] = getAccEffAndErr(year, cg, Bngs1[i-1],Bngs1[i])
            tmps=tmpHandle(year, cg)
            tmps.createTmps(0, sys_uncers, massCutH=Bngs, isMultiBin=True)
            tmps.saveTmps(tmpName)
            writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff)
            #cmd='text2workspace.py -P HiggsAnalysis.CombinedLimit.FRatioPerBinModel:FRatioPerBinModel datacards/%s.txt --channel-masks -o datacards/%s.root'%(cardName, cardName)
            #os.system(cmd)
            impactOut="Impact_multiBins_"+year+"_"+cg
            #plotImpact(cardName, impactOut, False, True)
            for i in range(9,10):
                #cmd="combine -M MultiDimFit --algo=grid --floatOtherPOIs 1 -P r_bin%s --points=300   --setParameterRanges r_bin%s=0,3 -d  datacards/%s.root   "%(str(i),str(i),cardName)
                #os.system(cmd)
                #cmd="mv higgsCombineTest.MultiDimFit.mH120.root   combineOutputs/testMultiBins.root"
                #os.system(cmd)
                runCB(scanRange, fileName, i, cardName) 
                inputs={"result":fileName+str(i)}
                plotNll(year, cg, 0, False, plotName, i, **inputs)
                frs=getFrAndLimits(fileName+str(i),i)
                FRmed[key].append(str(frs[2]))
                FRhigh[key].append(str(frs[3]))
                FRlow[key].append(str(frs[1]))

    FRmed["allYearCombine"]=[]
    FRmed["allYearCombine_bb"]=[]
    FRmed["allYearCombine_be"]=[]    
    FRlow["allYearCombine"]=[]
    FRlow["allYearCombine_bb"]=[]
    FRlow["allYearCombine_be"]=[]
    FRhigh["allYearCombine"]=[]
    FRhigh["allYearCombine_bb"]=[]
    FRhigh["allYearCombine_be"]=[]
    for i in range(9,10):        
        runCB(scanRange, "allYearCombine_mulitBins", i, *cardNames)
        if i==9:
            impactOut="Impact_mulitBins_allYearCombine"
            #plotImpact("combinedCard", impactOut, False, True)
        frs=getFrAndLimits("allYearCombine_mulitBins"+str(i),i)
        inputs={"result":"allYearCombine_mulitBins"+str(i)}
        plotNll("all", "all", 0, False, "allYearCombine_mulitBins", i, **inputs)
        FRmed["allYearCombine"].append(str(frs[2]))
        FRhigh["allYearCombine"].append(str(frs[3]))
        FRlow["allYearCombine"].append(str(frs[1]))
        runCB(scanRange, "allYearCombine_mulitBins_bb", i, *cardNames_bb)
        if i==9:
            impactOut="Impact_multiBins_allYearCombine_bb"
            #plotImpact("combinedCard", impactOut, False, True)
        inputs={"result":"allYearCombine_mulitBins_bb"+str(i)}
        plotNll("all", "bb", 0, False, "allYearCombine_mulitBins", i, **inputs)
        frs=getFrAndLimits("allYearCombine_mulitBins_bb"+str(i),i)
        FRmed["allYearCombine_bb"].append(str(frs[2]))
        FRhigh["allYearCombine_bb"].append(str(frs[3]))
        FRlow["allYearCombine_bb"].append(str(frs[1]))
        runCB(scanRange, "allYearCombine_mulitBins_be", i, *cardNames_be)
        inputs={"result":"allYearCombine_mulitBins_be"+str(i)}
        plotNll("all", "be", 0, False, "allYearCombine_mulitBins", i, **inputs)
        if i==9:
            impactOut="Impact_multiBins_allYearCombine_be"
            #plotImpact("combinedCard", impactOut, False, True)
        inputs={"result":"allYearCombine_mulitBins_be"+str(i)}
        frs=getFrAndLimits("allYearCombine_mulitBins_be"+str(i),i)
        FRmed["allYearCombine_be"].append(str(frs[2]))
        FRhigh["allYearCombine_be"].append(str(frs[3]))
        FRlow["allYearCombine_be"].append(str(frs[1]))

    print(FRlow)
    print(FRmed)
    print(FRhigh)
    #writeTxt("multiBins_low", FRlow)
    #writeTxt("multiBins_med", FRmed)
    #writeTxt("multiBins_high", FRhigh)
  
if __name__=="__main__":
    main()
