import os

def plotImpact(datacard, output, isfix=True, isMultiBins=False):

    if isMultiBins:
        cmd='text2workspace.py -P HiggsAnalysis.CombinedLimit.FRatioPerBinModel:FRatioPerBinModel datacards/%s.txt --channel-masks -o datacards/%s.root'%(datacard, datacard)
    else:
        cmd= "text2workspace.py datacards/%s.txt datacards/%s.root"%(datacard, datacard)
    os.system(cmd) 
    cmd= "combineTool.py -M Impacts --allPars -d datacards/%s.root -m 125   "%datacard
    if isfix:
        arg1="--doInitialFit -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
        arg2="--doFits -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic"
        arg3="--autoBoundsPOIs r -t -1 --toysFrequentist --expectSignal 1 --X-rtd MINIMIZER_analytic -o impacts.json"
        prefix="_fixed"
    else:
        arg1="--X-rtd MINIMIZER_analytic --doInitialFit --setParameterRanges r_bin1=0.0,5.0:r_bin2=0.0,5.0:r_bin3=0.0,5.0:r_bin4=0.0,5.0:r_bin5=0.0,5.0:r_bin6=0.0,5.0:r_bin7=0.0,5.0:r_bin8=0.0,5.0:r_bin9=0.0,5.0:"
        arg2="--X-rtd MINIMIZER_analytic --doFits --setParameterRanges r_bin1=0.0,5.0:r_bin2=0.0,5.0:r_bin3=0.0,5.0:r_bin4=0.0,5.0:r_bin5=0.0,5.0:r_bin6=0.0,5.0:r_bin7=0.0,5.0:r_bin8=0.0,5.0:r_bin9=0.0,5.0"
        arg3="--X-rtd MINIMIZER_analytic -o impacts.json "
        prefix="_floated"
    os.system(cmd+arg1)
    os.system(cmd+arg2)
    os.system(cmd+arg3)
    if isMultiBins: 
        for i in range(1, 10):
            cmd="plotImpacts.py -i impacts.json --POI r_bin"+str(i)+" -o "+output+"bin"+str(i)+prefix
            os.system(cmd)
        cmd="mv *.pdf plots/Impacts/"
        os.system(cmd)

    else:
        cmd="plotImpacts.py -i impacts.json -o "+output+prefix
        os.system(cmd)
        cmd="mv %s.pdf plots/Impacts/"%(output+prefix)
        os.system(cmd)
