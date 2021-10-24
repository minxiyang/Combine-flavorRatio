import os

def runCB(scanRange, output, *args):

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
        cardtext=cardtext.replace("datacards//depot", "/depot")
        combinedCard=open("datacards/combinedCard.txt", "w")
        combinedCard.write(cardtext)
        combinedCard.close()
        
        datacard="combinedCard"
        print(msg)
    else:
        datacard=args[0]
        print("run combine for datacard "+datacard)

    cmd = "combine -M MultiDimFit datacards/%s.txt --algo grid --rMin %s --rMax %s --points 1000 > log.txt"%(datacard, str(scanRange[0]), str(scanRange[1]))
    os.system(cmd)
    cmd="mv higgsCombineTest.MultiDimFit.mH120.root combineOutputs/%s.root"%output
    os.system(cmd)    

