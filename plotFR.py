import ROOT
from plotting.plotBinByBinFR import plotBinByBinFR
import json
from Parameters import def_bng as bng 
from Parameters import heur_FR, heur_err


def main():

    lowFile="multiBins_low_run2And3.txt"
    medFile="multiBins_med_run2And3.txt"
    highFile="multiBins_high_run2And3.txt"

    lows=json.loads(open("txtResults/"+lowFile, "r").read())
    meds=json.loads(open("txtResults/"+medFile, "r").read())
    highs=json.loads(open("txtResults/"+highFile, "r").read())

    for year in ['2016', '2017', '2018']:
        for cg in ['bb', 'be']:
            key=year+cg
            lowStr=lows[key]
            medStr=meds[key]
            highStr=highs[key]
            low=[float(x) for x in lowStr]
            med=[float(x) for x in medStr]
            high=[float(x) for x in highStr]
            plotBinByBinFR(year, cg, bng, med, low, high) 

    for cg in ['bb', 'be', "all"]:
        #if cg == "all":key="allYearCombine"
        #else: key="allYearCombine_"+cg
        if cg== "all": key="run2And3Combine"
        else: key="run2And3Combine_"+cg
        
        lowStr=lows[key]
        medStr=meds[key]
        highStr=highs[key]
        low=[float(x) for x in lowStr]
        med=[float(x) for x in medStr]
        high=[float(x) for x in highStr]
        plotBinByBinFR("Run2and3", cg, bng, med, low, high, heur_FR[cg], heur_err[cg])


if __name__=="__main__":
    main()
   
         

              
