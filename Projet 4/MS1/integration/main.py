import numpy as np
from scipy.integrate import dblquad

lda = (3*10**8)/(2.4*10**9)
k = 2*np.pi/lda

def f(th, phi):
    return (np.cos(0.15 * k * lda * np.sin(th) * np.cos(phi))) ** 2 * (
        (np.cos(th)) ** 2 * (np.sin(phi)) ** 2 + (np.cos(phi)) ** 2)*np.sin(th)

if __name__ == '__main__':
    int = dblquad(f, 0, 2*np.pi, 0, np.pi)
    print(int)