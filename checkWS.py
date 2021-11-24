import ROOT


f=ROOT.TFile.Open("datacards/combinedCard.root")
ws=f.Get("w")
#ws.SetDirectory(0)
f.Close()
objs=ws.allGenericObjects()
pdfs=ws.allPdfs()
pdfs.Print()
for obj in objs:

    name=obj.GetName()
    print(name)
    #obj.Print()

#snap=pdfs.snapshot() 
#print(snap)
#for i in range(10):

#   obj=objs.at(i)
#    name=obj.GetName()
#    print(name)
















