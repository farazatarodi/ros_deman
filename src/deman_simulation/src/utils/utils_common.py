import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def generate3DPoints(start, length, limit):

    x = [np.random.randint(1, limit) for i in range(length)]
    y = [np.random.randint(1, limit) for i in range(length)]
    z = [np.random.randint(1, limit) for i in range(length)]

    x.insert(0, start[0])
    y.insert(0, start[1])
    z.insert(0, start[2])

    return x, y, z


def calculateDistance(x, y, z):
    distance = []
    for i in range(len(x)-1):
        d = math.sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2+(z[i+1]-z[i])**2)
        distance.append(d)

    print('Distances:', distance)

    return np.sum(distance)


def draw3DPath(coordinates, pathCoordinates, path):
    pathX, pathY, pathZ = pathCoordinates
    x, y, z = coordinates

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    for i in path:
        ax.text(x[i], y[i], z[i], i)

    ax.plot(pathX, pathY, pathZ)

    plt.show()
