from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import *
from numpy import *
from matplotlib import pyplot as plt
import math
from tkinter import *
from matplotlib.pyplot import figure



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
    
##################################################################################################################
with open(name_file, 'r') as file:
    file_lst = file.readlines()

    for i in range(len(file_lst)):
        file_lst[i] = file_lst[i].split("\t")

    tableau = array(file_lst[1:]).transpose()
    datas = []
    for i in range(len(tableau)):
        datas.append(tableau[i].astype(float))
    
    nbr_g = len(datas)
    couleur = ["b","g","r","c","m","y","orange"]
    graphe_name = value.get()
    k = 0
    f = plt.figure()
    while k <nbr_g-1:
        plt.plot(datas[0]*10**3,datas[1+k], color = couleur[k%7])
        axes = plt.axes()
        axes.set_ylim([-15,15])
        plt.xlabel(r'Temps [ms]')
        plt.ylabel(r'Tension [V]')
        plt.title(graphe_name)
        plt.grid(True,ls="-")
        k+=1
f.show()

