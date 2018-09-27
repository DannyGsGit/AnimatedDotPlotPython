import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def main():
    numframes = 10
    numpoints = 30

    hist = np.zeros(numpoints) + 1.0
    y = np.arange(1, numpoints)
    x = np.arange(-15, numpoints-15)
    X, Y = np.meshgrid(x, y)

    # color_data = np.random.random((numframes, numpoints))
    c = Y <= hist

    fig = plt.figure()
    scat = plt.scatter(X, Y, c=c, s=50, cmap="Greys")

    ani = animation.FuncAnimation(fig,
                                  update_plot,
                                  frames=numframes,
                                  fargs=(hist, Y, scat))
    plt.show()

def update_plot(i, hist, Y, scat):
    # Randomly pick an index of hist to increment
    idx = round(np.random.normal(20, 2, size=1)[0],0).astype('int')
    idx = np.clip(idx, 0, 29)
    hist[idx] = np.clip(hist[idx] + 1, 0, 30)
    c = Y <= hist
    print(hist)
    scat.set_array(c.flatten())
    return scat

main()