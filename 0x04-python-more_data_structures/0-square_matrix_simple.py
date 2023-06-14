#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    bigList = []
    for eachLi in matrix:
        sqList = list(map(lambda x: x ** 2, eachLi))
        bigList.append(sqList)
    return bigList
