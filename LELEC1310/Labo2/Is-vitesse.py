import numpy as np
import matplotlib.pyplot as plt


def Is(N, Ns, U, Rs, Rr, Rp, Xe, Xu):
    Is = np.zeros(len(N))
    ind = 0
    for i in N:
        gamma = (Ns-i)/Ns
        num = np.sqrt((Rp*(Rs+Rr/gamma)-Xu*Xe)**2+(Xe*Rp+Xu*Rp+Xu*(Rs+Rr/gamma))**2)
        den = Xu*Rp*np.sqrt(((Rs+Rr/gamma)**2+Xe**2))
        Is[ind] = U*num/den
        ind+=1
    return Is


if __name__ == '__main__':
    Rp = 370.9
    Rr = 1.929
    Rs = 1.5
    Xe = 3.22
    Xu = 32.11
    U = 230/np.sqrt(3)
    Ns = 1500
    N = np.linspace(1, 1500, 1000)
    Ist = Is(N, Ns, U, Rs, Rr, Rp, Xe, Xu)

    IsMesure = np.array([5.432, 5.2, 4.75, 4.5, 4.316, 4.26, 4.26])
    NMesure = np.array([1410, 1420, 1430, 1440, 1450, 1458, 1465])
    IsTh = Is([1410, 1420, 1430, 1440, 1450, 1458, 1465], Ns, U, Rs, Rr, Rp, Xe, Xu)
    Error = (IsTh-IsMesure)
    Errorsq = (IsTh-IsMesure)**2
    print(Errorsq)
    print(sum(Errorsq)/len(Errorsq))

    plt.figure()
    plt.scatter(NMesure, IsMesure, c='r')
    plt.plot(N, Ist)
    plt.xlabel("N [tr/min]")
    plt.ylabel("Is [A]")
    plt.grid()
    plt.show()
