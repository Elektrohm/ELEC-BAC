import numpy as np
import matplotlib.pyplot as plt


def carson(Am, Fm, kf):
    beta = kf*Am/Fm
    return 2*Fm*(1+beta)


if __name__ == '__main__':
    kf = 25e3
    Am = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
    Fm = np.array([5e3, 7.5e3, 10e3, 20e3, 50e3, 75e3, 100e3, 125e3])

    BAm = np.array([60e3, 80e3, 110e3, 130e3, 160e3, 180e3, 210e3, 230e3])
    BFm = np.array([60e3, 60e3, 60e3, 80e3, 100e3, 150e3, 200e3, 250e3])

    x = np.linspace(5e3, 150e3, 1000)
    Bfmth = carson(1, x, kf)

    a, b = np.polyfit(Fm, BFm, 1)

    plt.figure()
    plt.scatter(Fm/(10**3), BFm/(10**3), marker="s", c="blue", label="Labview")
    plt.plot(x/(10**3), Bfmth/(10**3), color="red", label="Formule de Carson")
    plt.plot(x/(10**3), (a*x+b)/(10**3), color='blue', label="régression linéaire")
    plt.title("Analyse de la formule de Carson Am=1V, kf=25kHz/V")
    plt.xlabel("Fm [kHz]")
    plt.ylabel("Largeur de bande [kHz]")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()