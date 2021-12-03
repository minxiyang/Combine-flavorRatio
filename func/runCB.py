import os

def runCB(scanRange, output, i, *args):

    if len(tuple(args))>1:
   
        cmd="combineCards.py "
        msg="run combine for combined datacard "
        for arg in args: 
            cmd+=(arg+"=datacards/"+arg+".txt   ")
            msg+=" "+arg
        cmd+=" > datacards/combinedtext.txt"
        os.system(cmd)
        cardfile=open("datacards/combinedtext.txt", "r")
        cardtext=cardfile.read()
        cardfile.close()
        cardtext=cardtext.replace("datacards/templates", "templates")
        combinedCard=open("datacards/combinedCard.txt", "w")
        combinedCard.write(cardtext)
        combinedCard.close()
        
        datacard="combinedCard"
       
    else:
        datacard=args[0]
        print("run combine for datacard "+datacard)
    if i>0:
        cmd='text2workspace.py -P HiggsAnalysis.CombinedLimit.FRatioPerBinModel:FRatioPerBinModel datacards/%s.txt --channel-masks -o datacards/%s.root'%(datacard, datacard)
        os.system(cmd)
        #cmd="combine -M MultiDimFit --algo=grid --floatOtherPOIs 1 -P r_bin%s --points=300  --setParameterRanges r_bin%s=%s,%s -d  datacards/%s.root --X-rtd MINIMIZER_analytic  "%(str(i), str(i), str(scanRange[0]), str(scanRange[1]), datacard)
        cmd="combine -M MultiDimFit --algo=grid --floatOtherPOIs 1 -P r_bin%s --points=300  --setParameterRanges r_bin%s=%s,%s -d  datacards/%s.root  --X-rtd MINIMIZER_analytic"%(str(i), str(i), str(scanRange[0]), str(scanRange[1]), datacard)
        output=output+str(i)
    else:
        cmd = "combine -M MultiDimFit datacards/%s.txt --algo grid --rMin %s --rMax %s --points 300 --X-rtd MINIMIZER_analytic > log.txt"%(datacard, str(scanRange[0]), str(scanRange[1]))
    os.system(cmd)
    cmd="mv higgsCombineTest.MultiDimFit.mH120.root combineOutputs/%s.root"%output
    os.system(cmd)    

