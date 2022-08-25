import math
from utils.utils_common import calculateDistance, generate3DPoints
from utils.utils_conveyorForX import drawPath
import json

headSpeed = 1  # unit/s
conveyorSpeed = 1  # unit/s
screwTime = 1  # second
zThreshold = 1000000

Y_FACTOR = 84000/242


def ConveyorForX():
    coordinatesFile = open('src/deman_tsp/laptop data/3.json')
    coordinatesData = json.load(coordinatesFile)
    xs = [0]
    ys = [0]
    zs = [0]
    cs = [0]
    for point in coordinatesData:
        xs.append(0)
        ys.append(math.floor(point[1]*Y_FACTOR))
        zs.append(0)
        cs.append(math.floor(point[0]*15810-11000000))

    path = list(range(0, len(xs)))
    sortedCs = cs.copy()
    print(path)
    for i in range(len(sortedCs)):
        for j in range(0, len(sortedCs)-i-1):
            if sortedCs[j] < sortedCs[j+1]:
                sortedCs[j], sortedCs[j+1] = sortedCs[j+1], sortedCs[j]
                path[j], path[j+1] = path[j+1], path[j]

    print('X: ', xs)
    print('Y: ', ys)
    print('Z: ', zs)
    print('C: ', cs)
    print('Path: ', path)

    return drawPath(xs, ys, zs, cs, zThreshold, path)


print(ConveyorForX())
