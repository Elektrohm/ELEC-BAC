from numpy import *
from matplotlib import pyplot as plt
"""
x = array([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
y = array([0.303,0.451,0.618,0.806,1.02,1.267,1.554,1.89,2.34,3.087,3.424,3.711,3.958,4.174,4.363,4.53,4.679,4.812,5])
"""

x = array([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
y = array([1.5,2.25,3,3.75,4.5,5.25,6,6.75,7.5,8.25,9,9.75,10.5,11.25,12,12.75,13.5,14.25,15])

m, b = polyfit(x,y,1)
text = "{}.x + {}".format(m,b)

plt.plot(x,y,'o')
plt.plot(x,m*x+b, label = text)
plt.legend()

plt.xlabel("Duty-cycle [%]")
plt.ylabel("Tension de sortie du passe bas [V]")
plt.title("Relation entre duty-cycle et tension de sortie du passe bas")

plt.show()