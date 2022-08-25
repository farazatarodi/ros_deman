#!/usr/bin/env python3

import math
from re import S
from concorde.tsp import TSPSolver
from utils.utils_regional import draw3DPath
import json

zThreshold = 1000000

X_FACTOR = 54000/365
Y_FACTOR = 84000/242


def Regional():
    coordinatesFile = open('src/deman_tsp/laptop data/1.json')
    coordinatesData = json.load(coordinatesFile)

    xs = [0]
    ys = [0]

    for point in coordinatesData:
        xs.append(math.floor(point[0]*X_FACTOR))
        ys.append(math.floor(point[1]*Y_FACTOR))

    sortedXs = xs.copy()
    sortedYs = ys.copy()
    sortedIndex = [i for i in range(len(xs))]

    for i in range(len(sortedXs)):
        for j in range(0, len(sortedXs)-i-1):
            if sortedXs[j] < sortedXs[j+1]:
                sortedXs[j], sortedXs[j+1] = sortedXs[j+1], sortedXs[j]
                sortedYs[j], sortedYs[j+1] = sortedYs[j+1], sortedYs[j]
                sortedIndex[j], sortedIndex[j +
                                            1] = sortedIndex[j+1], sortedIndex[j]

    firstXs = []
    for i in range(math.floor(len(sortedXs)/2)):
        firstXs.append(sortedXs[i]-sortedXs[math.floor(len(sortedXs)/2)-1])
    secondXs = sortedXs[math.floor(len(sortedXs)/2):]

    firstYs = sortedYs[:math.floor(len(sortedYs)/2)]
    secondYs = sortedYs[math.floor(len(sortedYs)/2):]

    firstZs = [0]
    firstCs = [
        math.floor(-11000000+sortedXs[math.floor(len(sortedXs)/2)-1]*15810/X_FACTOR)]
    for x in firstXs:
        firstZs.append(0)
        firstCs.append(
            math.floor(-11000000+sortedXs[math.floor(len(sortedXs)/2)-1]*15810/X_FACTOR))

    secondZs = []
    secondCs = []
    for x in secondXs:
        secondZs.append(0)
        secondCs.append(-11000000)

    solver = TSPSolver.from_data(firstXs, firstYs, 'EUC_2D')
    solution = solver.solve()
    firstPath = solution.tour

    solver = TSPSolver.from_data(secondXs, secondYs, 'EUC_2D')
    solution = solver.solve()
    secondPath = solution.tour

    print('First Xs: ', firstXs)
    print('First Ys: ', firstYs)
    print('First Zs: ', firstZs)
    print('First Cs: ', firstCs)
    print('First path: ', firstPath)
    print('Second Xs: ', secondXs)
    print('Second Ys: ', secondYs)
    print('Second Zs: ', secondZs)
    print('Second Cs: ', secondCs)
    print('Second path: ', secondPath)

    firstPathX, firstPathY, firstPathZ, firstPathC = draw3DPath(
        firstXs, firstYs, firstZs, firstCs, zThreshold, firstPath)
    secondPathX, secondPathY, secondPathZ, secondPathC = draw3DPath(
        secondXs, secondYs, secondZs, secondCs, zThreshold, firstPath)

    return firstPathX+secondPathX, firstPathY+secondPathY, firstPathZ+secondPathZ, firstPathC+secondPathC


print(Regional())
