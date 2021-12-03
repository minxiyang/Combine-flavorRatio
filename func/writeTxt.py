from json import dumps
from func.timer import timer


def writeTxt(fileName, _dict):
    
    for key in _dict.keys(): 
        for i in range(len(_dict[key])):
            _dict[key][i]=str(_dict[key][i])

    localTime=timer()
    fileName=fileName+"_"+localTime+".txt"
    with open("txtResults/"+fileName, "w") as txt:
        txt.write(dumps(_dict))
