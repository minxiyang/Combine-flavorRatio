import os

def plotImpact(datacard, output, isfix=True):

    cmd= "text2workspace.py datacards/%s.txt datacards/%s.root"%(datacard, datacard)
    os.system(cmd) 
    cmd= "combineTool.py -M Impacts -d datacards/%s.root -m 125   "%datacard
    if isfix:
        arg1="--doInitialFit -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
        arg2="--doFits -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
        arg3="--autoBoundsPOIs r -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic -o impacts.json"
        prefix="_fixed"
    else:
        arg1=" --doInitialFit --robustFit 1"
        arg2=" --doFits --robustFit 1"
        arg3=" -o impacts.json"
        prefix="_floated"
    os.system(cmd+arg1)
    os.system(cmd+arg2)
    os.system(cmd+arg3)
    
    cmd="plotImpacts.py -i impacts.json -o "+output+prefix
    os.system(cmd)
    cmd="mv %s.pdf plots/Impacts/"%(output+prefix)
    os.system(cmd)
