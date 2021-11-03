import ROOT

def makeSimpleDatacard():
    hGen=ROOT.TH1D("hgen","hgen",9,0,9)
    hReco=ROOT.TH1D("hreco","hreco",9,0,9)
    hBkg=ROOT.TH1D("hbkg","hbkg",9,0,9)
    hResp=ROOT.TH2D("hresp","hresp",9,0,9,9,0,9)
    hData=ROOT.TH1D("hdata","hdata",9,0,9)
    '''make a binned datacard to match the 1D ML unfolding.
    This are C&C datacards no syst.'''
    #global hGen,hReco,hResp,hBkg
    datacard=open("datacard.txt","w")
    datacard.write("## Automatically generated. Simple C&C datacard model.\n")
    datacard.write("## Original author: Andrea Carlo Marini\n ##Adapted for Flavor ratio by Arnab")
    datacard.write("* imax\n")
    datacard.write("* jmax\n")
    datacard.write("* kmax\n")
    datacard.write("----------------\n")
    datacard.write("bin ")
    for ireco in range(1,hReco.GetNbinsX()+1):
        datacard.write("Reco_%d "%ireco)
    datacard.write("\n")
    datacard.write("observation ")
    for ireco in range(1,hReco.GetNbinsX()+1):
        datacard.write("%d "%(hData.GetBinContent(ireco)))
    datacard.write("\n")
    datacard.write("----------------\n")
    cleanup=True
    datacard.write("bin ")
    for ireco in range(1,hReco.GetNbinsX()+1):
        for igen in range(1,hGen.GetNbinsX()+1):
            # remove un-necessary processes
            #if cleanup and hResp.GetBinContent(ireco,igen)<0.01: continue
            datacard.write("Reco_%d "%ireco) ##sig igen, in reco ireco
        datacard.write("Reco_%d "%ireco)## bkg
    datacard.write("\n")
    datacard.write("process ")
    for ireco in range(1,hReco.GetNbinsX()+1):
        for igen in range(1,hGen.GetNbinsX()+1):
            #if cleanup and hResp.GetBinContent(ireco,igen)<0.01: continue
            datacard.write("gen_bin%d "%igen) ##sig igen, in reco ireco
        datacard.write("Bkg ")## bkg
    datacard.write("\n")
    datacard.write("process ")

    for ireco in range(1,hReco.GetNbinsX()+1):
        for igen in range(1,hGen.GetNbinsX()+1):
            #if cleanup and hResp.GetBinContent(ireco,igen)<0.01: continue
            datacard.write("%d "%(-igen)) ## 0 -1, -2 --> for signal
        datacard.write("1 ")## bkg >0 for bkg
    datacard.write("\n")
    datacard.write("rate ")
    for ireco in range(1,hReco.GetNbinsX()+1):
        for igen in range(1,hGen.GetNbinsX()+1):
            #if cleanup and hResp.GetBinContent(ireco,igen)<0.01: continue
            datacard.write("%.2f "% (hResp.GetBinContent(ireco,igen)))
        datacard.write("%.2f "%(hBkg.GetBinContent(ireco)))##
    datacard.write("\n")
    datacard.write("----------------\n")


if __name__ == "__main__" :
    makeSimpleDatacard()
