import numpy as np
import matplotlib.pyplot as plt

def drawContinuousPath(xs, ys, zs, cs, z_limit, path):
    pathX = []
    pathY = []
    pathZ = []
    pathC = []

    for i in path:
        if np.where(path == i) == 0:
            pathX.append(xs[i])
            pathY.append(ys[i])
            pathZ.append(zs[i])
            ax.text(xs[i], ys[i], zs[i], i)

            pathX.append(xs[i])
            pathY.append(ys[i])
            pathZ.append(z_limit)
            ax.text(xs[i], ys[i], z_limit, i)

        elif np.where(path == i) == len(path):
            pathX.append(xs[i])
            pathY.append(ys[i])
            pathZ.append(z_limit)
            ax.text(xs[i], ys[i], z_limit, i)

            pathX.append(xs[i])
            pathY.append(ys[i])
            pathZ.append(zs[i])
            ax.text(xs[i], ys[i], zs[i], i)

        else:
            pathX.append(xs[i])
            pathY.append(ys[i]+(i)*deltaYHead+(i-1)*deltaYScrew)
            pathZ.append(z_limit)
            ax.text(xs[i], ys[i]+(i)*deltaYHead+(i-1)*deltaYScrew, z_limit, i)

            pathX.append(xs[i])
            pathY.append(ys[i]+(i)*deltaYHead+(i-1)*deltaYScrew)
            pathZ.append(zs[i])
            ax.text(xs[i], ys[i]+(i)*deltaYHead+(i-1)*deltaYScrew, zs[i], i)

            pathX.append(xs[i])
            pathY.append(ys[i]+i*(deltaYHead+deltaYScrew))
            pathZ.append(zs[i])
            ax.text(xs[i], ys[i]+i*(deltaYHead+deltaYScrew), zs[i], i)

            pathX.append(xs[i])
            pathY.append(ys[i]+i*(deltaYHead+deltaYScrew))
            pathZ.append(z_limit)
            ax.text(xs[i], ys[i]+i*(deltaYHead+deltaYScrew), z_limit, i)

    ax.plot(pathX, pathY, pathZ)

    plt.show()

    return pathX, pathY, pathZ


