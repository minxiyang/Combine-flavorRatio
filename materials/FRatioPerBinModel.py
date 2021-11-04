from HiggsAnalysis.CombinedLimit.PhysicsModel import *
massBins = [200, 300, 400, 500, 690, 900, 1250, 1610, 2000, 3500]
class FRatioPerBinModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        poi_names = []
        for i in range(len(massBins)-1):
            self.modelBuilder.doVar("r_bin"+str(i+1)+"[1,0.01,10]")
            poi_names.append("r_bin"+str(i+1))
        self.modelBuilder.doSet("POI", ",".join(poi_names))

    def getYieldScale(self, bin, process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        for i in range(len(massBins)-1):
            #if process=="gen_bin"+str(i+1):
            if process=="mu_DY_S"+str(i+1):
                print "Scaling %s/%s by r_bin%d" % (bin, process, i+1)
                return "r_bin"+str(i+1)
        return 1

FRatioPerBinModel = FRatioPerBinModel()
