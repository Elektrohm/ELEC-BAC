import numpy as np
import matplotlib.pyplot as plt


def théorie(phi):
    return np.arcsin(phi*1/90)

abscisse = [-90,-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
ordonnée = [-1.55,-1.35,-1.18,-1.05,-0.939,-0.835,-0.735,-0.640,-0.559,-0.493,-0.436,-0.379,-0.323,-0.266,-0.209,-0.153,-0.096,-0.04,0.019,0.075,0.131,0.187,0.244,0.300,0.355,0.411,0.468,0.528,0.601,0.690,0.788,0.890,0.996,1.114,1.266,1.45,1.566]

phi = np.linspace(-90,90,1000)

def show(phi):
    plt.figure()
    plt.plot(phi,théorie(phi), color = "green")
    plt.stem(abscisse,ordonnée)
    plt.xlabel(r"$\phi$")
    plt.ylabel(r"$\alpha$")
    plt.grid()
    plt.show()
    
show(phi)