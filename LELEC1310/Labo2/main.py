import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


# measured values
P = np.array([80, 70, 80, 84, 100, 125, 150, 190])
Is = np.array([1.9, 0.992, 1.112, 1.36, 1.384, 2.13, 2.6, 3.16])
N = np.array([1300, 1426, 1450, 1460, 1464, 1467, 1468, 1470])

# circuit parameters
Rs = 1.5
Cut = 0.09

# Y = Pelec - 3RsIs - Cutwm, X = Ul
Y = P-3*Rs*Is-Cut*N*2*np.pi/60
X = np.array([29.5, 50, 75, 100, 125, 150, 175, 200])


# Wanted function form
def func(params, x):
    a, b = params
    return a * x * x + b


# Error function, that is, the difference between the value obtained by fitting curve and the actual value
def error(params, x, y):
    return func(params, x) - y


# Solving parameters
def solvePara():
    # first candidate
    p0 = [0.5, 45]
    Para = leastsq(error, p0, args=(X, Y))
    return Para


# Output the final result
def solution():
    Para = solvePara()
    a, b = Para[0]
    print(f"a= {a:.4f},  b={b:.4f}")
    print("Fitted curve equation:")
    print(f"y= {a:.6f}x²+ {b:.4f}")
    print(f"Rp = {1/a}, Cp = {b*2/(2*np.pi*50)}")

    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, color="green", label="sample data", linewidth=2)

    # Drawing Fitted Lines
    x = np.linspace(0, 230, 1000)
    y = a * x * x + b # # function
    plt.plot(x, y, color="red", label=r"$\dfrac{U_l^2}{R_p}+ C_p\dfrac{\omega_s}{p}$", linewidth=2)
    plt.xlabel(r"$U_l [V]$")
    plt.ylabel(r"$P-3R_sI_s-C_{ut}\omega_m [W]$")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    solution()