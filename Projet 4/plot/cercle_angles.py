import numpy as np
import matplotlib.pyplot as plt


def plot_circle(dmax, ax):
    for x in range(2, dmax+4, 4):
        circle = plt.Circle((0.0, 0.0), x, fill=False)
        ax.add_artist(circle)
        ax.text(0, x-0.5, f"{x}m")


def plot_angles(dmax, ax, nmbr_of_angles=4):
    """
    dessine nmbr of angles lignes sur le plot
    :param dmax: distance maximal visible par le radar
    :param ax: axes d'une plt.figure()
    :param nmbr_of_angles: nombre d'angles que l'on veut afficher
    :return: /
    """
    step = 180//nmbr_of_angles
    for i in range(-90, 90+step, step):
        x = [0.0, 2*dmax*np.sin(i*np.pi/180)]
        y = [0.0, 2*dmax*np.cos(i*np.pi/180)]
        plt.plot(x, y, color='blue')
        ax.text(3*np.sin(i*np.pi/180), 3*np.cos(i*np.pi/180), f"{i}°")


def background(dmax, nmbr_of_angles):
    """
    Construit le background avec les cercles et nmbr_of_angles + ligne d'angles
    :param dmax: distance maximal visible par le radar
    :param nmbr_of_angles: nombre de ligne d'angles souhaité
    :return: /
    """
    plt.figure()
    ax = plt.gca()

    plot_circle(dmax, ax)
    plot_angles(dmax, ax, nmbr_of_angles)

    # set x-y axis and aspect
    plt.xlim([-dmax - 2, dmax + 2])
    plt.ylim([0, dmax + 2])
    ax.set_aspect(1)  # make aspect ratio square
    plt.grid()


def target(d, phi):

    # plots target line
    # plt.plot([0.0, d*np.sin(phi*np.pi/180)], [0.0, d*np.cos(phi*np.pi/180)], color='red')
    plt.scatter(d*np.sin(phi*np.pi/180), d*np.cos(phi*np.pi/180), marker='x', s=80, c='r')


if __name__ == '__main__':
    dmax = 50  # [m]
    d = 7.5 #[m]
    phi = 15 #[°]
    vmax = 5  # [m/s]
    background(dmax, 6)
    target(d, phi)
    plt.show()