import numpy as np
import matplotlib.pyplot as plt


def h(t, a):
    if t == 0:
        return (1/T) * (1+a(4/np.pi - 1))
    if t == T/(4*a) or t == -T/(4*a):
        return a/(T*np.sqrt(2)) * ((1+2/np.pi)*np.sin(np.pi/(4*a)) + (1-2/np.pi) * np.cos(np.pi/(4*a)))
    else:
        num1 = np.sin(np.pi*(1-a)*t/(T))
        num2 = 4*a*t/T*np.cos(np.pi*(1+a)*t/T)
        den = np.pi*(t/T)*(1-(4*a*t/T)**2)
        return 1/T*(num1+num2)/den


def G(f, a):
    if abs(f*T) <= (1/2)*(1-a):
        return T
    if abs(f*T) >= (1/2)*(1-a) and abs(f*T) <= (1/2)*(1+a):
        return (T/2)*(1+np.cos((np.pi/a)*(abs(f*T)-(1-a)/2)))
    else:
        return 0


def square(f):
    if f >= -1/2 and f <= 1/2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    T = 1
    time = np.linspace(-6*T, 6*T, 500)
    f = np.linspace(-1.25/T, 1.25/T, 500)
    y = np.zeros(len(f))
    a = [0.1, 0.25, 0.5, 0.75, 1]
    col = ["r", "g", "b", "orange", "magenta"]
    plt.figure()
    for v, i in enumerate(a):
        for j in range(len(f)):
            y[j] = np.sqrt(G(f[j], i))
        plt.plot(f, y, col[v], label=r"$\alpha = $"+str(i))

    for j in range(len(f)):
        y[j] = square(f[j])
    plt.plot(f, y, color="black", linestyle="--")

    plt.xlabel(r"$\frac{1}{T}$")
    plt.ylabel("|G(f)|")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()
