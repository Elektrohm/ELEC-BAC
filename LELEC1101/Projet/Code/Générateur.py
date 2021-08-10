import matplotlib.pyplot as plt
import numpy as np


def triangle(X):
    tension = np.zeros(len(X))
    dx = X[1]-X[0]
    tension[-1]=7.5
    for i in range(0,len(X)):
        if (X[i]%T<T/2):
            tension[i] = tension[i-1] + (-15/2*dx*10**(-3))/(R*C)
        if (X[i]%T>=T/2):
            tension[i] = tension[i-1] + (15/2*dx*10**(-3))/(R*C)
    return tension

def carré(X):
    tension = np.zeros(len(X))
    for i in range(0,len(X)):
        if (X[i]%T<T/2):
            tension[i] = 15
        if (X[i]%T>=T/2):
            tension[i] = -15
    return tension
    
    

def show(x):
    plt.figure()
    plt.title("Fonctionnement du générateur")
    plt.plot(x,triangle(x), color = "green")
    plt.plot(x,carré(x), color = "blue")
    plt.xlabel("temps [µs]")
    plt.ylabel("tension [V]")
    plt.grid()
    plt.show()

d = 0.001
T = 0.4
R = 1000
C = 0.0000001
X = np.arange(0,1.200+d,d)
show(X)