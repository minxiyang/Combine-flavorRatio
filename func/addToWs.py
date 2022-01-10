import ROOT


def addToWs(ws, obj):

    getattr(ws, 'import')(obj, ROOT.RooCmdArg())
