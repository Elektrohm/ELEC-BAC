import numpy as np 
from matplotlib import pyplot as plt 

_Rr = 1.9
Rs = 1.5
ws = 100*np.pi
p = 2
Vs = 230/np.sqrt(3)
_Xe = 3.22


def Cem_theorique(x):
    gamma = 1 - x/1500
    c = (3*p)/ws * gamma * _Rr * (Vs**2) / ((gamma*Rs + _Rr)**2 + (gamma*_Xe)**2)
    return c


speed = [1410, 1420, 1430, 1440, 1450, 1458, 1465]
Cem   = [8.2, 7, 5.7, 4.1, 2.69, 1.87, 0.7]
Cemth = Cem_theorique(np.array(speed))
print(Cemth)
error = Cemth-Cem
print(sum(error)/len(Cemth))
errorsq = error**2


x = np.linspace(0, 1500, 200)

plt.scatter(speed, Cem, color='r', label='Mesures expérimentales')
plt.plot(x, Cem_theorique(x), label=r'Courbe théorique')

plt.xlabel(r'$\omega_m$ [tr/min]')
plt.ylabel(r'$c_{ut}$ [Nm]')

plt.legend(loc = 'lower left')

plt.grid()

plt.show()
