import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd


def SuperPlot(x, y, xlegend, ylegend, ylabel):
    X = x[np.logical_not(np.isnan(x))]
    X2 = x[np.logical_not(np.isnan(y))]
    Y = y[np.logical_not(np.isnan(y))]
    plt.plot(X, X, color='b', lw=1.5, zorder=1)
    plt.scatter(X2, Y, s=20, color='r', label=ylabel, zorder=2)
    plt.legend()
    plt.xlabel(xlegend)
    plt.ylabel(ylegend)
    plt.tight_layout()
    plt.grid()
    plt.show()


def allScatter(x, y, ylabel, r):
    X = x[np.logical_not(np.isnan(x))]
    X2 = x[np.logical_not(np.isnan(y))]
    Y = y[np.logical_not(np.isnan(y))]
    plt.plot(X, X, color='b', lw=1.5, zorder=1)
    plt.scatter(X2, Y, s=20, color=r, label=ylabel, zorder=2)


def allPlot(x, y, ylabel, r):
    X = x[np.logical_not(np.isnan(x))]
    X2 = x[np.logical_not(np.isnan(y))]
    Y = y[np.logical_not(np.isnan(y))]
    plt.plot(X, X, color='b', lw=1.5, zorder=1)
    plt.scatter(X2, Y, color=r, label=ylabel, zorder=2)


if __name__ == '__main__':
    # abscisse élévation
    elevation = np.array([10, 20, 30, 40])
    # expérimentaux pour d=2.8m
    elevation28 = np.array([10, 17, 33, 44])
    # expérimentaux pour d=4.2m
    elevation42 = np.array([9, 21, 33, np.nan])

    allPlot(elevation, elevation28, r"points expérimentaux d=2.8m", 'r')
    allPlot(elevation, elevation42, r"points expérimentaux d=4.6m", 'magenta')
    plt.xlabel(r"$\theta_{réel}[°]$")
    plt.ylabel(r"$\theta_{radar}[°]$")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()

    # abscisse azimuth
    angle = np.array([10, 20, 30, 40, 50, 60, 70])
    # expérimentaux 6m
    angle6 = np.array([9.5, 20, 29, 38, 50, 56, 73])
    
    SuperPlot(angle, angle6, r"$\varphi_{réel}[°]$", r"$\varphi_{radar}[°]$", r"points expérimentaux d=6m")
