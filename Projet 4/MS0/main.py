# MS0.npz must be loaded using numpy (np.load). The video is the scene that has been measured by the radar.

import numpy as np
import matplotlib.pyplot as plt


f_0 = 10e3  # [Hz]
x = lambda t: np.cos(2*np.pi*f_0*t)

if __name__ == '__main__':
    fs = 50e3
    Ns = 100
    t = np.arange(0, 0.501e-3, 0.001e-3)

    nTs = np.array([(i * 1 / fs) for i in range(Ns)])
    X = np.array([x(i) for i in nTs])

    # fft fait de lui même un zero padding ou crop de x
    dft = np.fft.fft(X, Ns)

    plt.plot(t, x(t))
    plt.stem(nTs, X)
    plt.show()