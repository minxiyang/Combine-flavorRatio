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
        print(msg)
    else:
        datacard=args[0]
        print("run combine for datacard "+datacard)
    cmd='text2workspace.py -P HiggsAnalysis.CombinedLimit.FRatioPerBinModel:FRatioPerBinModel datacards/%s.txt --channel-masks -o datacards/%s.root'%(datacard, datacard)
    os.system(cmd) 
    #cmd = "combine -M MultiDimFit datacards/%s.txt --algo grid --rMin %s --rMax %s --points 1000 --X-rtd MINIMIZER_analytic > log.txt"%(datacard, str(scanRange[0]), str(scanRange[1]))
    #cmd="combine -M MultiDimFit --algo singles -d datacards/%s.root -t 0"%datacard 
    #cmd="combine -M MultiDimFit --setParameters=r_bin1=1,r_bin2=1,r_bin3=1,r_bin4=1,r_bin5=1,r_bin6=1,r_bin7=1,r_bin8=1,r_bin9=1 --floatOtherPOIs=1   -t -1 -m 120 --algo=grid --points=1000 -P r_bin%s --setParameterRanges r_bin%s=0.01,10 --X-rtd MINIMIZER_analytic   datacards/%s.root"%(str(i),str(i),datacard)
    #cmd="combine -M MultiDimFit  --floatOtherPOIs=1   -t -1 -m 120 --algo=grid --points=1000 -P r_bin%s --setParameterRanges r_bin%s=0.01,10 --X-rtd MINIMIZER_analytic   datacards/%s.root"%(str(i),str(i),datacard)
    cmd="combine -M MultiDimFit --algo=grid --floatOtherPOIs 1 -P r_bin%s --points=300 --setParameterRanges r_bin%s=0,5 -d  datacards/%s.root   "%(str(i),str(i),datacard)
    os.system(cmd)
    cmd="mv higgsCombineTest.MultiDimFit.mH120.root combineOutputs/%s.root"%output
    os.system(cmd)    

