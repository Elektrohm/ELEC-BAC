import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as colors
import time

LOW_VAL = -10e3

#DATA = np.load('group6_distance2inverse_3.npz')
DATA = np.load('group6_distance_1.npz')
#DATA = np.load('group6_distance2_2.npz')
#DATA = np.load('group6_vitesse2_1.npz')

#DATA = np.load('group3_allerretourvcont_1.npz')

data = DATA['data']
background = DATA['background']
chirp = DATA['chirp']

print(chirp)
f0 = chirp[0]
B = chirp[1]
Ns = chirp[2]
Nr = chirp[3]
Ts = chirp[4]
Tr = chirp[5]

c = 3e8
Dw = 2*np.pi*B
w_0 = 2*np.pi*f0+(B/2)

def v_max(T):
    return np.pi*c/(T*w_0)

def d_max(T):
    return np.pi*c*T/(Ts*Dw)

def vToM(vect, Nr, Ns):
    rep = np.zeros((int(Nr), int(Ns)), dtype=np.complex_)
    for i in range((int(Nr))):
        for j in range(int(Ns)):
            rep[i][j] = vect[i*int(Ns) + j] - background[i][j]
    return rep

def getLine(m, i):
    return m[i]

def getColumn(m, i):
    n = len(m)
    rep = np.zeros(n, dtype=np.complex_)
    for j in range(n):
        rep[j] = m[j][i]
    return rep

def setLine(m, i, line):
    m[i] = line

def setColumn(m, i, column):
    for j in range(len(m)):
        m[j][i] = column[j]

def applyFFTLine(m, i):
    l = np.fft.fft(getLine(m, i))
    setLine(m, i, l)

def applyFFTColumn(m, i):
    c = np.fft.fft(getColumn(m, i))
    setColumn(m, i, c)

def removeLowValue(m, val):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (m[i][j] < val):
                m[i][j] = val



mat = vToM(data[0], Nr, Ns)

print(v_max(Tr))
x = np.linspace(-v_max(Tr)/2, v_max(Tr)/2, int(Nr))
y = np.linspace(0, d_max(Tr), int(Ns))



'''
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print()
print(getLine(mat, 1))
print(getColumn(mat, 1))
setColumn(mat, 2, [1,2,3,4])
print(mat)
'''

for i in range(len(mat)):
    applyFFTLine(mat, i)

for i in range(len(mat[0])):
    applyFFTColumn(mat, i)

removeLowValue(mat, LOW_VAL)

plt.pcolormesh(x, y, mat.T.real, cmap='Greys')
plt.colorbar()

plt.xlabel("Vitesse [m/s]")
plt.ylabel("Distance [m]")

plt.ion()

plt.pause(2)

for i in range(1, len(data)):
    mat = vToM(data[i], Nr, Ns)
    for i in range(len(mat)):
        applyFFTLine(mat, i)
    for i in range(len(mat[0])):
        applyFFTColumn(mat, i)
    removeLowValue(mat, LOW_VAL)
    plt.pcolormesh(x, y, mat.T.real, cmap='Greys')
    plt.draw()
    plt.pause(Tr)

plt.ioff()
plt.show()
