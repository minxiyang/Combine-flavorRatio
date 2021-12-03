from func.tmpHandle import tmpHandle
from func.writeDatacards import writeDatacards
from func.getAccEffAndErr import getAccEffAndErr
from func.runCB import runCB
from plotting.plotNll import plotNll
from plotting.plotTmps import plotTmps
from Parameters import sys_uncers 
from func.getFrAndLimits import getFrAndLimits
from plotting.plotFrVsCut import plotFrVsCut
from func.writeTxt import writeTxt

def main():

    scanRange=(0, 5.)
    massCuts=range(400, 1201, 200)
    #massCuts=[1250]
    frsLeft2={}
    frsLeft1={}
    frsMed={}
    frsRight1={}
    frsRight2={}

    print("produce flavor ratio as a function of the mass cutoff")
    for massCut in massCuts:
        cardNames=[]
        for year in ["2016","2017","2018", "Run3"]:
            for cg in ["bb","be"]:
                if year=="Run3": scale="Run3"
                else: scale="Run2" 
                key=year+cg
                cardName="ch"+year+cg+"_"+str(massCut)+"cut"
                tmpName="tmp"+year+cg+"_"+str(massCut)+"cut"
                fileName="output"+year+cg+"_"+str(massCut)+"cut"
                plotName="nll"+year+cg+"_"+str(massCut)+"cut"
                cardNames.append(cardName)
                acc_eff = getAccEffAndErr(year, cg, massCut)
                if year=="Run3":tmps=tmpHandle("2018", cg, scale=scale)
                else: tmps=tmpHandle(year, cg, scale=scale)
                tmps.createTmps(massCut, sys_uncers)

                tmps.saveTmps(tmpName)
                #plotTmps(year, cg, tmps.templates)
                
                writeDatacards(cardName, tmpName, year, cg, tmps.templates, acc_eff)
                runCB(scanRange, fileName, 0, cardName)
                fr=getFrAndLimits(fileName, 0)
                print(fr)
                inv=0.2
                #while fr[0]==0. or fr[4]==0.:
                #    print("rerun combine")
                #    print((fr[2]-inv, fr[2]+inv)) 
                #    runCB((fr[2]-inv, fr[2]+inv), fileName, 0, cardName)
                #    fr=getFrAndLimits(fileName, 0)
                #    inv=inv*0.9
                #    print(fr)
                if key in frsLeft2.keys(): frsLeft2[key].append(fr[0])
                else: frsLeft2[key]=[fr[0]]
                if key in frsLeft1.keys(): frsLeft1[key].append(fr[1])
                else: frsLeft1[key]=[fr[1]]
                if key in frsMed.keys(): frsMed[key].append(fr[2])
                else: frsMed[key]=[fr[2]]
                if key in frsRight1.keys(): frsRight1[key].append(fr[3])
                else: frsRight1[key]=[fr[3]]
                if key in frsRight2.keys(): frsRight2[key].append(fr[4])
                else: frsRight2[key]=[fr[4]]        
                 
            
            
        runCB(scanRange, "Run2and3Combine", 0, *cardNames)
        fr=getFrAndLimits("Run2and3Combine")
        print(fr)
        inv=0.2
        #while fr[0]==0. or fr[4]==0.:
        #    print("rerun combine")
        #    print((fr[2]-inv, fr[2]+inv))
        #    runCB((fr[2]-inv, fr[2]+inv), fileName, 0, *cardNames)
        #    fr=getFrAndLimits(fileName, 0)
        #    inv=inv*0.9
        #    print(fr)

        key="Run2and3Combine"
        if key in frsLeft2.keys(): frsLeft2[key].append(fr[0])
        else: frsLeft2[key]=[fr[0]]
        if key in frsLeft1.keys(): frsLeft1[key].append(fr[1])
        else: frsLeft1[key]=[fr[1]]
        if key in frsMed.keys(): frsMed[key].append(fr[2])
        else: frsMed[key]=[fr[2]]  
        if key in frsRight1.keys(): frsRight1[key].append(fr[3])
        else: frsRight1[key]=[fr[3]]
        if key in frsRight2.keys(): frsRight2[key].append(fr[4])
        else: frsRight2[key]=[fr[4]]

    writeTxt("frByCutL2",frsLeft2)
    writeTxt("frByCutL1",frsLeft1)
    writeTxt("frByCutM",frsMed)
    writeTxt("frByCutR1",frsRight1)
    writeTxt("frByCutR2",frsRight2)
    print(frsLeft1)
    print(frsMed)
    print(frsRight1)
    print(frsRight2)
    for year in ["Run3"]:
        for cg in ["bb","be"]:
            key=year+cg
            plotFrVsCut(frsLeft2[key], frsLeft1[key], frsMed[key], frsRight1[key], frsRight2[key], massCuts, key+"v2")

    key="Run2and3Combine"    
    plotFrVsCut(frsLeft2[key], frsLeft1[key], frsMed[key], frsRight1[key], frsRight2[key], massCuts, "Run2and3Combinev2")    

if __name__=="__main__":
    main()
