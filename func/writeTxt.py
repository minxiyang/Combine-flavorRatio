from json import dumps
from func.timer import timer


def writeTxt(fileName, _dict):
    
    localTime=timer()
    fileName=fileName+"_"+localTime+".txt"
    with open("txtResults/"+fileName, "w") as txt:
        txt.write(dumps(_dict))
