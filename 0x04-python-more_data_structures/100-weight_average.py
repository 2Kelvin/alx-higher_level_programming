#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weightMul = 0
    forAver = 0
    for eTup in my_list:
        eTupList = list(eTup)
        weightMul += (eTupList[0] * eTupList[1])
        forAver += eTupList[1]
    return weightMul / forAver
