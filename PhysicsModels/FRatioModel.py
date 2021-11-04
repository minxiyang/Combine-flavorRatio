from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class FRatioModel(PhysicsModel):
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("r[1,0.01,10]")
        self.modelBuilder.doSet("POI", ",".join(['r']))

    def getYieldScale(self, bin, process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"
        if self.DC.isSignal[process]:
            print 'Scaling %s/%s by r' % (bin, process)
            return "r"
        return 1

FRatioModel = FRatioModel()
