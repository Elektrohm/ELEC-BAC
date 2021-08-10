import numpy as np 
from matplotlib import pyplot as plt
import cmath as cm

_Rr = 1.9
Rs = 1.5
Rp = 370.9
ws = 100*np.pi
p = 2
Vs = 230/np.sqrt(3)
_Xe = 3.22
X_mu = 32.11


def cosphi_theorique(x):
    gamma = 1 - x/1500
    val = (Vs/np.sqrt(3)) * (1/(_Rr/gamma + Rs + 1j*_Xe) + 1/Rp + 1/(1j*X_mu))
    arg = np.angle(val)
    return np.cos(arg)


speed  = [1410, 1420, 1430, 1440, 1450, 1458, 1465]
cosphi = [0.739, 0.676, 0.634, 0.502, 0.407, 0.324, 0.206]
cosphith = cosphi_theorique(np.array(speed))
print(cosphith)
error = cosphith-cosphi
errorsq = error**2
print(errorsq)
print(sum(errorsq)/len(errorsq))

x = np.linspace(0, 1499, 200)

plt.scatter(speed, cosphi, color='r', label='Mesures expérimentales')
plt.plot(x, cosphi_theorique(x), label='Théorique')

plt.xlabel(r'$\omega_m$ [tr/min]')
plt.ylabel(r'cos($\varphi$) [-]')

plt.legend(loc = 'lower left')

plt.grid()

plt.show()