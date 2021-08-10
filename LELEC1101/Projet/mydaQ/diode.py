from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import *
from numpy import *
from matplotlib import pyplot as plt
import math
from matplotlib.pyplot import figure

###########################################################################################################
#Graphe théorique Générateur :
d = 0.001
T = 0.4
R = 1000
C = 0.0000001
absc = arange(0,2+d,d)

###########################################################################################################

fenetre = Tk()

l = LabelFrame(fenetre, text="Nom du graphe", padx=20, pady=20)
l.pack(fill="both", expand="yes")

value = StringVar() 
entree = Entry(l, textvariable=value, width=30)
entree.pack()

l2 = LabelFrame(fenetre, text="Fichier", padx=20, pady=15)
l2.pack(fill="both", expand="yes")


def select_file():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    global name_file
    name_file = filename
select=Button(l2, text="Selectionner un fichier", command=select_file)
select.pack()

def exit():
    fenetre.destroy()
bouton=Button(fenetre, text="Let's plot", command=exit)
bouton.pack()

fenetre.mainloop()


###########################################################################################################

class data(): #Données du graphe
    def __init__(self,X,Y,nameX,nameY):
            
        y = zeros(len(Y))
        for i in range(len(Y)):
            y[i]=float(Y[i].replace(",", ".").strip("\n"))
            
        self.X = X
        self.Y = y
        self.nameX = nameX #Nom de l'abscisse 
        self.nameY = nameY #Nom de l'ordronnée
        
    def __str__(self):
        return str(self.X) + str(self.Y)     
        
########################################################################################################### 

with open(name_file, 'r') as file:
    file_lst = file.readlines()

    for i in range(len(file_lst)):
        file_lst[i] = file_lst[i].split("\t")

    lst = array(file_lst[5:]).transpose()
    Datas = []
    dt = float(file_lst[2][1].replace(",", "."))
    i = 0
    while i < len(lst)-1:
        time = arange(0,dt*(len(lst[i])-1),dt)*10e2
        Datas.append(data(time,lst[i+1,1:],"",""))
        i+= 2
            
#---------------------------------------------------------------------------------------------------------# 

    nbr_g = len(Datas)
    couleur = ["b","g","r","c","m","y","orange"]
    graphe_name = value.get()
    k = 0
    while k <1:
        plt.plot(Datas[k+1].Y,Datas[k].Y, color = couleur[k%7])
        plt.xlabel("Temps [ms]")
        plt.ylabel("Tension [V]")
        plt.title(graphe_name)
        plt.grid(True,ls="-")
        k+=1
    
#---------------------------------------------------------------------------------------------------------#
    
x = Datas[1].Y
y = Datas[0].Y
a,b,c,d = polyfit(x,y,3)

R1 = 1
R2 = 1
R3 = 2.39
R4 = 1
R5 = 0.39
R6 = 0.39
R7 = 1

def vd(vin):
    return a*vin**3+b*vin**2+c*vin+d

def v1(vin):
    return -R2*(vin/R1+vd(vin)/R3)

def vout(vin):
    print(vd(vin))
    print(v1(vin))
    print(vd(vd(v1(vin))))
    return -R7*(v1(vin)/R4+vd(vd(v1(vin)))/R5)

print(vout(1))






        
        







