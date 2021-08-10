from numpy import *
from scipy.special import erfc
import matplotlib.pyplot as plt

SNR_MIN = 0
SNR_MAX = 10
Eb_No_dB = arange(SNR_MIN, SNR_MAX+1)
SNR = 10**(Eb_No_dB/10.0)  # linear SNR

x = linspace(SNR_MIN, SNR_MAX, 1000)
x = 10**(x/10.0)
print((1/2)*erfc(sqrt(7)))
BER_BPSK = (1/2)*erfc(sqrt(SNR))
BER_QPSK = (1/2)*erfc(sqrt(SNR/2))
BER = empty(shape(SNR))

plt.semilogy(Eb_No_dB, BER_BPSK, 'r', linewidth=2)
plt.semilogy(Eb_No_dB, BER_QPSK, 'b', linewidth=2)

BPSK = array([8.5229e-2, 5.771e-2, 3.8636e-2, 2.3348e-2, 1.2935e-2, 6.177e-3, 2.413e-3, 8.16e-4, 2.28e-4, 5.1e-5, 6e-6])
QPSK = array([0.15976, 0.13808, 0.10615, 8.172e-2, 5.88e-2, 3.942e-2, 2.513e-2, 1.371e-2, 6.2e-3, 2.6e-3, 8.7e-4])

plt.scatter(Eb_No_dB, BPSK, color='r')
plt.scatter(Eb_No_dB, QPSK, color='b')
plt.grid(True, which="both")
plt.title("BER moyen pour une BPSK/QPSK")
plt.legend(('BER BPSK', 'BER QPSK', 'sample BPSK', "sample QPSK"))
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.tight_layout()
plt.show()