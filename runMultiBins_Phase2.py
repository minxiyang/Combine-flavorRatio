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
    for year in ["Phase2"]:
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
            if year == "Phase2":tmps=tmpHandle("2018", cg, scale="Phase2")
            else: tmps=tmpHandle(year, cg)
            tmps.createTmps(0, sys_uncers, massCutH=Bngs, isMultiBin=True)
            tmps.saveTmps(tmpName)
            writeDatacards(cardName, tmpName, "Run3", cg, tmps.templates, acc_eff)
            #cmd='text2workspace.py -P HiggsAnalysis.CombinedLimit.FRatioPerBinModel:FRatioPerBinModel datacards/%s.txt --channel-masks -o datacards/%s.root'%(cardName, cardName)
            #os.system(cmd)
            impactOut="Impact_multiBins_"+year+"_"+cg
            #plotImpact(cardName, impactOut, False, True)
            for i in range(1,10):
                runCB(scanRange, fileName, i, cardName) 
                inputs={"result":fileName+str(i)}
                plotNll(year, cg, 0, False, plotName, i, **inputs)
                frs=getFrAndLimits(fileName+str(i),i)
                FRmed[key].append(str(frs[2]))
                FRhigh[key].append(str(frs[3]))
                FRlow[key].append(str(frs[1]))

    FRmed["phase2Combine"]=[]
    FRmed["phase2Combine_bb"]=[]
    FRmed["phase2Combine_be"]=[]    
    FRlow["phase2Combine"]=[]
    FRlow["phase2Combine_bb"]=[]
    FRlow["phase2Combine_be"]=[]
    FRhigh["phase2Combine"]=[]
    FRhigh["phase2Combine_bb"]=[]
    FRhigh["phase2Combine_be"]=[]
    for i in range(1,10):        
        runCB(scanRange, "phase2Combine_mulitBins", i, *cardNames)
        if i==9:
            impactOut="Impact_mulitBins_allYearCombine"
            #plotImpact("combinedCard", impactOut, False, True)
        frs=getFrAndLimits("phase2Combine_mulitBins"+str(i),i)
        inputs={"result":"phase2Combine_mulitBins"+str(i)}
        plotNll("all", "all", 0, False, "phase2Combine_mulitBins", i, **inputs)
        FRmed["phase2Combine"].append(str(frs[2]))
        FRhigh["phase2Combine"].append(str(frs[3]))
        FRlow["phase2Combine"].append(str(frs[1]))

    print(FRlow)
    print(FRmed)
    print(FRhigh)
    writeTxt("multiBins_low", FRlow)
    writeTxt("multiBins_med", FRmed)
    writeTxt("multiBins_high", FRhigh)
  
if __name__=="__main__":
    main()
