import numpy as np
from Parameters import data_files
import math

def getBngs(flavor, year, cg, masscut):

    files=data_files

    if flavor == "mu": files = [file_ for file_ in files if 'dimuon' in file_ or 'clean' in file_]
    else: files = [file_ for file_ in files if 'ele' in file_]

    if year == "2016":    files=[file_ for file_ in files if 'Mordion2017' in file_ or '2016' in file_]
    elif year == "2017":  files=[file_ for file_ in files if '_2017' in file_]
    else:                 files=[file_ for file_ in files if '_2018' in file_]

    if cg == "bb": files=[file_ for file_ in files if 'bb' in file_ or 'BB' in file_]
    else:          files=[file_ for file_ in files if 'be' in file_ or 'BE' in file_]

    datafile=files[0]
    eventList=[]
    f=open("dataList/"+datafile,"r")
    for m in f:

        m=float(m)
        eventList.append(m)

    f.close()
    eventList.sort()
    miniSize=10
    miniN=20
    bins=[]
    bins.append(3500)
    ith=0
    delta_ith=0
    eventList.reverse()
    for i in range(len(eventList)):
        delta_ith+=1
        if (eventList[ith]-eventList[i])>miniSize and delta_ith>miniN and eventList[i]>masscut:
            binEdge=math.ceil(eventList[i])
            bins.append(binEdge)
            ith=i
            delta_ith=0
        elif eventList[i]<masscut:
            bins[-1]=masscut
            break
    bins.reverse()
    bng=np.asarray(bins,dtype=np.float64)
    return bng

