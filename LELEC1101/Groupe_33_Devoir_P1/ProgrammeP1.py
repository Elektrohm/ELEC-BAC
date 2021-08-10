#Programme fait pour le cours LELEC1101 dans le cadre du problème 1.
#Réalisé par le groupe 33 : Andi Ziberi, Thibault Grégoir, Loïc Grumiaux, Théo Denis
#18-02-2020

import numpy as np
from math import *
import matplotlib.pyplot as plt

#Constante utilisée pour les calculs :
T = 1  #période d'une seconde
V = 1  #tension du signal
S = 2  #variable définie pour respecter la contrainte V/S=0.5


#Fonction triangle écrite à l'aide des séries de Fourier
def u(t):
    U = np.zeros(len(t))
    for i in range(len(t)):
        U[i] = (8*V)/(pi**2)*(cos(2*pi/T*t[i])+cos(6*pi/T*t[i])/9+cos(10*pi/T*t[i])/25)
    return U

#Fonction triangle écrite à l'aide des séries de Fourier qui calcule pour plus de termes
def f(t):
    U = np.zeros(len(t))
    for i in range(len(t)):
        cosinus = Sum(t[i])
        U[i] = (8*V)/(pi**2)*cosinus
    return U

#Fonction subsidiaire qui calcule la somme des cosinus
def Sum(t):
    somme = 0
    for i in range(1,300):
        somme += (cos(2*(2*i-1)*pi/T*t))/((2*i-1)**2)
    return somme

#Fonction correspondant à l'approximation de Taylor d'ordre 3 de la fonction h(x).
def y(t):
    return u(t)-(u(t))**3/(2*S**2)

#Fonction correspondant à l'approximation de Taylor d'ordre 3 de la fonction h(x) pour plus de termes.
def yopp(t):
    return f(t)-(f(t))**3/(2*S**2)

def plotfig(x):
    plt.figure()
    #avec uniquement 3 harmoniques
    plt.plot(x,y(x),'-b',label='Fonction y(t) avec 3 harmoniques')
    plt.plot(x,u(x),'-r',label='Fonction u(t) avec 3 harmoniques')
    plt.legend()
    plt.xlabel("temps en secondes")
    plt.ylabel("tension de sortie")
    plt.show()
    
    #avec 300 harmoniques
    plt.plot(x,yopp(x),'-b',label='Fonction y(t) avec 300 harmoniques')
    plt.plot(x,f(x),'-r',label='Fonction u(t) avec 300 harmoniques')
    plt.legend()
    plt.xlabel("temps en secondes")
    plt.ylabel("tension de sortie")
    plt.show()
    
x = np.linspace(-2,2,2000)
plotfig(x)
    
    



