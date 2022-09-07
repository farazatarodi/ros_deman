#!/usr/bin/env python3

from concorde.tsp import TSPSolver
from utils.utils_stopAndMove import draw3DPath
import json

zThreshold = -20

CON_FACTOR = 1/1000


def convertCoords(coordinates):
    return round(coordinates*CON_FACTOR, 3)


def StopAndMove():
    coordinatesFile = open('src/deman_tsp/laptop data/1.json')
    coordinatesData = json.load(coordinatesFile)

    xs = [0]
    ys = [0]
    zs = [convertCoords(-30)]
    cs = [convertCoords(410)]
    for point in coordinatesData:
        xs.append(convertCoords(point[0]))
        ys.append(convertCoords(point[1]))
        zs.append(convertCoords(-30))
        cs.append(convertCoords(410))

    solver = TSPSolver.from_data(xs, ys, 'EUC_2D')
    solution = solver.solve()
    path = solution.tour

    print('X: ', xs)
    print('Y: ', ys)
    print('Z: ', zs)
    print('C: ', cs)
    print('Path: ', path)

    return draw3DPath(xs, ys, zs, cs, zThreshold, path)
