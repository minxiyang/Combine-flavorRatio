import os
import subprocess
import numpy as np
import glob



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
        cardtext=cardtext.replace("datacards/datacards", "datacards")
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
        cmd="combine -M MultiDimFit --algo=grid --floatOtherPOIs 1 -P r_bin%s --points=100  --setParameterRanges r_bin%s=%s,%s -d  datacards/%s.root  --X-rtd MINIMIZER_analytic"%(str(i), str(i), str(scanRange[0]), str(scanRange[1]), datacard)
        output=output+str(i)
    else:
        #cmd = "combine -M MultiDimFit datacards/%s.txt --algo grid --rMin %s --rMax %s --points 150 --X-rtd MINIMIZER_analytic"%(datacard, str(scanRange[0]), str(scanRange[1]))
        cmd = "combine -M MultiDimFit datacards/%s.txt --algo=singles  --robustFit 1 -t 300 --expectSignal=1 -s -1  --setRobustFitAlgo Minuit  --setParameterRanges r=0.25,4.0 --do95=1 --X-rtd MINIMIZER_analytic"%datacard
        #cmd = "combine -M MultiDimFit datacards/%s.txt --algo=singles -t 300 -s -1 --expectSignal=1 --robustFit 1 --setRobustFitAlgo Minuit  --setParameterRanges r=0.2,4.0 --do95=1 --X-rtd MINIMIZER_analytic"%datacard
        #cmd = "combine -M Significance datacards/%s.txt --signalForSignificance=1 --tries=100 "%datacard
        
    os.system(cmd)
    name=glob.glob("/depot/cms/users/minxi/lepratio/LimitSetting/ZprimetoMuMu/*root")
    #print(name)
    #subprocess.call(cmd)
    cmd="mv %s /depot/cms/users/minxi/lepratio/LimitSetting/ZprimetoMuMu/combineOutputs/%s.root"%(name[0],output)
    #os.system(cmd)
    cmd="rm -rf *root"
    #os.system(cmd)
    #subprocess.call(cmd)    

