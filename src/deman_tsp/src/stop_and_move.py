#!/usr/bin/env python3

import math
from concorde.tsp import TSPSolver
from utils.utils_common import calculateDistance, generate3DPoints
from utils.utils_stopAndMove import draw3DPath
import json

moveSpeed = 1 #unit/s
screwTime = 1 #second
zThreshold = 1000000

X_FACTOR = 54000/365
Y_FACTOR = 84000/242

def StopAndMove():
    coordinatesFile = open('src/deman_tsp/laptop data/3.json')
    coordinatesData = json.load(coordinatesFile)

    xs = [0]
    ys = [0]
    zs = [0]
    cs = [-11000000]
    for point in coordinatesData:
        xs.append(math.floor(point[0]*X_FACTOR))
        ys.append(math.floor(point[1]*Y_FACTOR))
        zs.append(0)
        cs.append(-11000000)


    solver = TSPSolver.from_data(xs, ys, 'EUC_2D')
    solution = solver.solve()
    path = solution.tour

    print('X: ', xs)
    print('Y: ', ys)
    print('Z: ', zs)
    print('C: ', cs)
    print('Path: ', path)

    return draw3DPath(xs, ys, zs, cs, zThreshold, path)
