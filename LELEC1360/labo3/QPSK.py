from numpy import *
from scipy.special import erfc
import matplotlib.pyplot as plt

SNR_MIN = 0
SNR_MAX = 10
Eb_No_dB = arange(SNR_MIN, SNR_MAX+1)
SNR = 10**(Eb_No_dB/10.0)  # linear SNR

Pe = empty(shape(SNR))
Corr = empty(shape(SNR))
BER = empty(shape(SNR))

def qfunc(x):
    return 0.5-0.5*erfc(x/sqrt(2))

loop = 0
for snr in SNR: # SNR loop
    # fonction Q
    Corr[loop] = 2*qfunc(sqrt(snr))-(qfunc(sqrt(snr)))**2
    Pe[loop] = 0.5 * erfc(sqrt(snr))
    VEC_SIZE = ceil(100/Pe[loop])  # vector length is a function of Pe

    # signal vector, new vector for each SNR value
    # bits either -1 or 1
    s = 2*random.randint(0, high=2, size=int(VEC_SIZE))-1

    # linear power of the noise; average signal power = 1
    # SNR = Es/N0, si puissance signal = 1 alors N0 = 1/SNR
    No = 1.0/snr

    # noise
    n = sqrt(No/2)*random.randn(int(VEC_SIZE))

    # signal + noise
    x = s + n

    # decode received signal + noise
    # sens maximum de vraisemblance = signe
    y = sign(x)

    # retourne indice où il y a des erreurs
    err = where(y != s)

    # si une erreur poids de 1 alors somme des erreurs = tailles vecteurs erreur
    error_sum = float(len(err[0]))

    # Bit Error Rate, nombre d'erreur / nombre de bits transmis
    BER[loop] = error_sum/VEC_SIZE
    loop += 1

print(Pe, Corr)
print(Pe*Corr)
#plt.semilogy(Eb_No_dB, Pe,'r',Eb_No_dB, BER,'s')
plt.semilogy(Eb_No_dB, Pe,'r',linewidth=2)
plt.semilogy(Eb_No_dB, Corr,linewidth=2)

labview = array([0.15976, 0.13808, 0.10615, 8.172e-2, 5.88e-2, 3.942e-2, 2.513e-2, 1.371e-2, 6.2e-3, 2.6e-3, 8.7e-4])
plt.semilogy(Eb_No_dB, labview,'-s')
plt.grid(True, which="both")
plt.title("BER moyen pour une BPSK")
plt.legend(('théorique', 'Corr', 'labview'))
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.show()