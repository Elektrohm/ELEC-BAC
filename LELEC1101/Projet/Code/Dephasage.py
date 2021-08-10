import matplotlib.pyplot as plt
import numpy as np


def deph(x):
    return 2*np.pi*1/4*np.sin(x)

def show(x):
    plt.figure()
    plt.title("Déphasage des signaux en fonction de l'angle d'incidence")
    plt.plot(x*180/np.pi,deph(x)*180/np.pi)
    plt.xlabel(r"Angle d'incidence $\alpha$")
    plt.ylabel(r"Déphasage entre les signaux $\phi$")
    plt.grid()
    plt.show()

d = 2*np.pi/100
x = np.arange(-np.pi/2,np.pi/2+d,d)
show(x)