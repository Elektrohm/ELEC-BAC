import matplotlib.pyplot as plt
import numpy as np


def quasisin(X,T):
    return 5.8*np.sin(2*np.pi/T*X)

def carré(X,T):
    tension = np.zeros(len(X))
    for i in range(0,len(X)):
        if (X[i]%T<T/2):
            tension[i] = 15
        if (X[i]%T>=T/2):
            tension[i] = -15
    return tension
    
    

def show(x,T,R,C):
    plt.figure()
    plt.title("Etage de puissance")
    plt.plot(x,quasisin(x,T), color = "green")
    plt.xlabel("temps [µs]")
    plt.ylabel("tension [V]")
    plt.grid()
    plt.show()

d = 1
T = 400
R = 1000
C = 0.0000001
X = np.arange(0,1200+d,d)
show(X,T,R,C)