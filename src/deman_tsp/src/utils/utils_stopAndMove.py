import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def draw3DPath(xs, ys, zs, cs, z_limit, path):
    pathX = []
    pathY = []
    pathZ = []
    pathC = []

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    for i in path:
        if np.where(path == i) == 0:
            for j in range(2):
                pathX.append(xs[i])
                pathY.append(ys[i])
                pathC.append(cs[i])

            pathZ.append(zs[i])
            pathZ.append(z_limit)

        elif np.where(path == i) == len(path):
            for j in range(2):
                pathX.append(xs[i])
                pathY.append(ys[i])
                pathC.append(cs[i])

            pathZ.append(z_limit)
            pathZ.append(zs[i])

        else:
            for j in range(3):
                pathX.append(xs[i])
                pathY.append(ys[i])
                pathC.append(cs[i])

            pathZ.append(z_limit)
            pathZ.append(zs[i])
            pathZ.append(z_limit)

        ax.text(xs[i], ys[i], zs[i], i)

    ax.plot(pathX, pathY, pathZ)

    # plt.show()

    return pathX, pathY, pathZ, pathC
