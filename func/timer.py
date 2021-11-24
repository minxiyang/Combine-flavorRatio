import datetime


def timer():

    dt = datetime.datetime.now()
    localTime = str(dt.month) + str(dt.day) + str(dt.hour) + str(dt.minute) + str(dt.second) 
    return localTime
