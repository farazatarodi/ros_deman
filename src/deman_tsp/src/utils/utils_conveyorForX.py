from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def drawPath(xs, ys, zs, cs, z_limit, path):
    pathX = []
    pathY = []
    pathZ = []
    pathC = []

    for i in path:
        if np.where(path == i) == 0:
            for j in range(2):
                pathX.append(0)
                pathY.append(ys[i])
                pathC.append(cs[i])


            pathZ.append(zs[i])
            pathZ.append(z_limit)

        elif np.where(path == i) == len(path):
            for j in range(2):
                pathX.append(0)
                pathY.append(ys[i])
                pathC.append(cs[i])

            pathZ.append(z_limit)
            pathZ.append(zs[i])

        else:
            for j in range(3):
                pathX.append(0)
                pathY.append(ys[i])
                pathC.append(cs[i])

            pathZ.append(z_limit)
            pathZ.append(zs[i])
            pathZ.append(z_limit)

    return pathX, pathY, pathZ, pathC

def generateHeadPath(ys, zs, zThreshold, path):
    pathY = []
    pathZ = []

    for i in path:
        if np.where(path == i) == 0:
            for j in range(2):
                pathY.append(ys[i])

            pathZ.append(zs[i])
            pathZ.append(zThreshold)

        elif np.where(path == i) == len(path):
            for j in range(2):
                pathY.append(ys[i])

            pathZ.append(zThreshold)
            pathZ.append(zs[i])

        else:
            for j in range(3):
                pathY.append(ys[i])

            pathZ.append(zThreshold)
            pathZ.append(zs[i])
            pathZ.append(zThreshold)

    return pathY, pathZ

def draw3DPath(coordinates, pathCoordinates, path):
    pathX, pathY, pathZ = pathCoordinates

    x, y, z = coordinates
    headX, headY, headZ = x, [0 for i in range(len(x))], z
    conveyorX, conveyorY, conveyorZ = [0 for i in range(len(y))], y, [0 for i in range(len(y))]

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    for i in path:
        ax.text(headX[i], headY[i], headZ[i], i)
        ax.text(conveyorX[i], conveyorY[i], conveyorZ[i], i)

    ax.plot(pathX, pathY, pathZ)
    ax.plot(conveyorX, conveyorY, conveyorZ)

    plt.show()
