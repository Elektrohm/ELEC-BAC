import numpy as np


def alpha(phi):
    value = np.arcsin(phi*1/90)
    text = "V = {} mV".format(value*10**3)
    return text,value*10**3

def erreur(Vobt,Vthe):
    text = "Erreur = {}°".format(abs((Vobt-Vthe)/10))
    return text

def run():
    loop = True
    while (loop):
        command = input("entrez exit ou un angle : ")
        value = command.split()[0]
        try:
            if value=="exit":
                print("A bientôt")
                loop = False
            else:
                text, value = alpha(int(value))
                print(text)
                Vobt = input("tension obtenue[mV] = ")
                print(erreur(float(Vobt),value))
            print() 
        except:
            print("entre une bonne commande fdp sinon je viens te niquer ta mère")
        
    
