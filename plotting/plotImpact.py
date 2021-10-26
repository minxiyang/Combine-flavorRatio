import os

def plotImpact(datacard, output):

    cmd= "text2workspace.py datacards/%s.txt datacards/%s.root"%(datacard, datacard)
    os.system(cmd) 
    cmd= "combineTool.py -M Impacts -d datacards/%s.root -m 125   "%datacard
    #arg1="--doInitialFit -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
    #arg2="--doFits -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
    #arg3="--autoBoundsPOIs r -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic -o impacts.json"
    arg1="--doInitialFit --robustFit 1"
    arg2="--robustFit 1 --doFits"
    arg3="-o impacts.json"
    os.system(cmd+arg1)
    os.system(cmd+arg2)
    os.system(cmd+arg3)
    cmd="plotImpacts.py -i impacts.json -o "+output
    os.system(cmd)
    cmd="mv %s.pdf plots/Impacts/"%output
    os.system(cmd)
