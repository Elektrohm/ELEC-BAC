import numpy as np


def computeDFT(fs, Ns):
    f_0 = 10e3
    x = lambda t: np.cos(2 * np.pi * f_0 * t)
    X = np.array([x(i * 1 / fs) for i in range(Ns)])

    # fft fait de lui même un zero padding ou crop de x
    dft = np.fft.fft(X, Ns)
    DFT = np.fft.fftshift(dft)

    # le pas dans rappel APE11 p53
    timestep = 2 * np.pi / Ns
    DFTfreqs = np.fft.fftfreq(Ns, d=timestep)
    wDFT = np.fft.fftshift(DFTfreqs)

    for i in range(0, len(wDFT)):
        wDFT[i] = wDFT[i] if abs(wDFT[i]) > 1e-9 else 0

    for i in range(0, len(DFT)):
        DFT[i] = DFT[i] if abs(DFT[i]) > 1e-9 else 0

    return DFT, wDFT


def plotSignal(DFT, wDFT):
    plt.figure()
    for i, var in enumerate(cas1):
        modDFT = np.abs(DFT[var])
        plt.subplot(3, 1, i + 1)
        plt.title(f"module de Y=FFT(X,{var})")
        plt.xlabel("freq ([rad])")
        plt.ylabel("|Y[k]| ([-])")
        plt.stem(wDFT[var], modDFT, linefmt=None, markerfmt=None, use_line_collection=True, basefmt=None, label="Y[k]")
        plt.legend(loc="best")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    X, Y = {}, {}
    cas1 = [100, 1000, 101]
    for i in cas1:
        Y[i], X[i] = computeDFT(50e3, 100)

    plotSignal(Y, X)