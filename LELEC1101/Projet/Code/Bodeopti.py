import control.matlab as ml
from scipy import signal
import numpy as np, matplotlib.pyplot as plt

    
#Fonction de transfert, ordre décroissant [1,2,3] -> s²+2s+3
num = np.array([1/(100**2),1/100,1])
den = np.array([10,2,1])


def plotBode(num,den,Nbrofpoints):
    """
    num = numérateur de la fonction de transfert
    den = dénominateur de la fonction de transfert
    nbrofpoints = nombre de points par décade où la fonction doit être évalué
    """
    s1 = signal.lti(num, den)
    s2 = signal.lti(num,[1])
    s3 = signal.lti([1],num)
    
    w, mag, phase = s1.bode(n=Nbrofpoints)
    w2, mag2, phase2 = s2.bode(n=Nbrofpoints)
    w3, mag3, phase3 = s3.bode(n=Nbrofpoints)
    
    fig, axs = plt.subplots(2)
    plt.subplots_adjust(hspace=0.5)
    
    #amplitude
    axs[0].set_title("Module de la fonction de transfert")
    axs[0].semilogx(w2, mag2)
    axs[0].set_xlabel("fréquence [kHz]")
    axs[0].set_ylabel("Amplitude ([dB])")
    axs[0].grid(True,which='both')
    #phase
    axs[1].set_title("Phase de la fonction de transfert")
    axs[1].semilogx(w2, phase2)
    axs[1].set_xlabel("fréquence [kHz]")
    axs[1].set_ylabel("Phase ([°])")
    axs[1].grid(True, which='both')
    
    plt.show()

plotBode(num,den,600)


