#!/usr/bin/env python3

import math
from concorde.tsp import TSPSolver
from utils.utils_common import calculateDistance, generate3DPoints
from utils.utils_stopAndMove import draw3DPath
import json

moveSpeed = 1 #unit/s
screwTime = 1 #second
zThreshold = 15

X_FACTOR = 54000/365
Y_FACTOR = 84000/360

def StopAndMove():
    # xs, ys, zs = generate3DPoints([0, 0, 0], 10, zThreshold)
    coordinatesFile = open('src/deman_tsp/laptop data/3.json')
    coordinatesData = json.load(coordinatesFile)

    xs = []
    ys = []
    zs = []
    for point in coordinatesData:
        xs.append(math.floor(point[0]*X_FACTOR))
        ys.append(math.floor(point[1]*Y_FACTOR))
        zs.append(0)


    solver = TSPSolver.from_data(xs, ys, 'EUC_2D')
    solution = solver.solve()
    path = solution.tour

    print('X: ', xs)
    print('Y: ', ys)
    print('Z: ', zs)
    print('Path: ', path)

    pathX, pathY, pathZ = draw3DPath(xs, ys, zs, zThreshold, path)

    print(pathX)

    return [xs[i] for i in path]
    # print(pathY)
    # print(pathZ)
    # distance = calculateDistance(pathX, pathY, pathZ)
    # print('Total distance:', distance)
    # print('Total time:', distance/moveSpeed + 10*screwTime , 'seconds')
