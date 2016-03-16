#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gautier.deleglise
#
# Created:     03/03/2016
# Copyright:   (c) gautier.deleglise 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from math import *
from numpy import *
import tkinter.filedialog
#Toutes les fonctions
#===========================

#Detection souris J1
def pointeurJ1(event):
    global bateaux1
    global bateau
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    print(casex)
    print(casey)
    if casex>1 and casey>1:
#MODE HORIZONTAL
        if mode=="h":
            if bateau==1:
                if casex<7:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0 and bateaux1[casey-2,casex+1]==0 and bateaux1[casey-2,casex+2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=3
                        bateaux1[casey-2,casex+1]=3
                        bateaux1[casey-2,casex+2]=4
                        bateau=2
            elif bateau==2:
                if casex<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0 and bateaux1[casey-2,casex+1]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=3
                        bateaux1[casey-2,casex+1]=4
                        bateau=3
            elif bateau==3:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=4
                        bateau=4
            elif bateau==4:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=4
                        bateau=5
            elif bateau==5:
                if casex<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=4
#MODE VERTICAL
        elif mode=="v":
            if bateau==1:
                if casey<7:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0 and bateaux1[casey+2,casex-2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-1,casex-2]=3
                        bateaux1[casey,casex-2]=3
                        bateaux1[casey+1,casex-2]=3
                        bateaux1[casey+2,casex-2]=4
                        bateau=2
            elif bateau==2:
                if casey<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-1,casex-2]=3
                        bateaux1[casey,casex-2]=3
                        bateaux1[casey+1,casex-2]=4
                        bateau=3
            elif bateau==3:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-1,casex-2]=3
                        bateaux1[casey,casex-2]=4
                        bateau=4
            elif bateau==4:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-1,casex-2]=3
                        bateaux1[casey,casex-2]=4
                        bateau=5
            elif bateau==5:
                if casey<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-1,casex-2]=4
        print(bateaux1)

#============================================================================
#Creation lignes dans window 1 et window2
def lignes1():
    #Lignes horizontale fenetre 1
    window1.create_line(500, 50, 0, 50, width=2)
    window1.create_line(500, 100, 0, 100, width=2)
    window1.create_line(500, 150, 0, 150, width=2)
    window1.create_line(500, 200, 0, 200, width=2)
    window1.create_line(500, 250, 0, 250, width=2)
    window1.create_line(500, 300, 0, 300, width=2)
    window1.create_line(500, 350, 0, 350, width=2)
    window1.create_line(500, 400, 0, 400, width=2)
    window1.create_line(500, 450, 0, 450, width=2)

#Lignes verticale fenetre 1
    window1.create_line(50, 0, 50, 500, width=2)
    window1.create_line(100, 0, 100, 500, width=2)
    window1.create_line(150, 0, 150, 500, width=2)
    window1.create_line(200, 0, 200, 500, width=2)
    window1.create_line(250, 0, 250, 500, width=2)
    window1.create_line(300, 0, 300, 500, width=2)
    window1.create_line(350, 0, 350, 500, width=2)
    window1.create_line(400, 0, 400, 500, width=2)
    window1.create_line(450, 0, 450, 500, width=2)

#Lettres horizontale fenetre 1
    window1.create_text(75,25,text='A')
    window1.create_text(125,25,text='B')
    window1.create_text(175,25,text='C')
    window1.create_text(225,25,text='D')
    window1.create_text(275,25,text='E')
    window1.create_text(325,25,text='F')
    window1.create_text(375,25,text='G')
    window1.create_text(425,25,text='H')
    window1.create_text(475,25,text='I')

#Chiffre vertical fenetre 1
    window1.create_text(25,75,text='1')
    window1.create_text(25,125,text='2')
    window1.create_text(25,175,text='3')
    window1.create_text(25,225,text='4')
    window1.create_text(25,275,text='5')
    window1.create_text(25,325,text='6')
    window1.create_text(25,375,text='7')
    window1.create_text(25,425,text='8')
    window1.create_text(25,475,text='9')
def ligne2():
#Ligne horizontale fenetre 2
    window2.create_line(500, 50, 0, 50, width=2)
    window2.create_line(500, 100, 0, 100, width=2)
    window2.create_line(500, 150, 0, 150, width=2)
    window2.create_line(500, 200, 0, 200, width=2)
    window2.create_line(500, 250, 0, 250, width=2)
    window2.create_line(500, 300, 0, 300, width=2)
    window2.create_line(500, 350, 0, 350, width=2)
    window2.create_line(500, 400, 0, 400, width=2)
    window2.create_line(500, 450, 0, 450, width=2)

#Ligne vertical fenetre 2
    window2.create_line(50, 0, 50, 500, width=2)
    window2.create_line(100, 0, 100, 500, width=2)
    window2.create_line(150, 0, 150, 500, width=2)
    window2.create_line(200, 0, 200, 500, width=2)
    window2.create_line(250, 0, 250, 500, width=2)
    window2.create_line(300, 0, 300, 500, width=2)
    window2.create_line(350, 0, 350, 500, width=2)
    window2.create_line(400, 0, 400, 500, width=2)
    window2.create_line(450, 0, 450, 500, width=2)


#Lettres horizontale fenetre 2
    window2.create_text(75,25,text='A')
    window2.create_text(125,25,text='B')
    window2.create_text(175,25,text='C')
    window2.create_text(225,25,text='D')
    window2.create_text(275,25,text='E')
    window2.create_text(325,25,text='F')
    window2.create_text(375,25,text='G')
    window2.create_text(425,25,text='H')
    window2.create_text(475,25,text='I')


#Chiffre vertical fenetre 2
    window2.create_text(25,75,text='1')
    window2.create_text(25,125,text='2')
    window2.create_text(25,175,text='3')
    window2.create_text(25,225,text='4')
    window2.create_text(25,275,text='5')
    window2.create_text(25,325,text='6')
    window2.create_text(25,375,text='7')
    window2.create_text(25,425,text='8')
    window2.create_text(25,475,text='9')
#Changer gamemode -> 0
def gm0():
    window1.delete(ALL)
    window2.delete(ALL)
    #MENU
    window1.create_image(0, 0, image = imagemenu, anchor = NW)
    BoutonJouer.place(relx = 0.8, rely =0.2, anchor = E)
    BoutonImporter.place(relx = 0.8, rely =0.27, anchor = E)
    BoutonRegles.place(relx = 0.8, rely =0.34, anchor = E)
    BoutonApropos.place(relx = 0.8, rely =0.41, anchor = E)
    BoutonQuitter.place(relx = 0.8, rely =0.48, anchor = E)
#Creation label
    LabelBienvenue = Label(Mafenetre, text = 'BIENVENUE !', fg = 'Blue')
    LabelBienvenue.pack()
#============================================================================
#Changer gamemode -> 1
def gm1():
    BoutonJouer.destroy()
    BoutonImporter.destroy()
    BoutonRegles.destroy()
    BoutonApropos.destroy()
    BoutonQuitter.destroy()
    window1.delete(ALL)
    window2.delete(ALL)
#Fenetre de jeu
    Largeur = 500
    Hauteur = 500
    img1 = window1.create_image(50,50,anchor=NW, image=photo)
    img2 = window2.create_image(50,50,anchor=NW, image=photo)

#Detection clic souris

    window1.bind("<Button-1>", pointeur)
#============================================================================
#Changer gamemode -> 2
def gm2():
    BoutonJouer.destroy()
    BoutonImporter.destroy()
    BoutonRegles.destroy()
    BoutonApropos.destroy()
    BoutonQuitter.destroy()
    window1.delete(ALL)
    window2.delete(ALL)
#============================================================================
#Changer gamemode -> 3
def gm3():
    BoutonJouer.destroy()
    BoutonImporter.destroy()
    BoutonRegles.destroy()
    BoutonApropos.destroy()
    BoutonQuitter.destroy()
    window1.delete(ALL)
    window2.delete(ALL)
#============================================================================
#Changer gamemode -> 4
def gm4():
    BoutonJouer.destroy()
    BoutonImporter.destroy()
    BoutonRegles.destroy()
    BoutonApropos.destroy()
    BoutonQuitter.destroy()
    window1.delete(ALL)
    window2.delete(ALL)
     #Fenetre de choix
    global joueur
    try:
        joueur
    except NameError:
        joueur=1
    #bateau:
    global bateau
    try:
        bateau
    except NameError:
        bateau=1

    #mode:
    #h= horizontal
    #v= vertical
    global mode
    try:
        mode
    except NameError:
        mode="h"

    img1 = window1.create_image(50,50,anchor=NW, image=photo)
    lignes1()

#Creation matrice
    global bateaux1
    bateaux1=zeros((9,9))
    bateaux1[8,6]=2
    bateaux1[8,7]=3
    bateaux1[8,8]=4
#Affichage bateau
    for x in range(0,9):
        for y in range(0,9):
            xvoul=x*50+50
            yvoul=y*50+50
            if bateaux1[y,x]==1:
                window1.create_image(xvoul,yvoul, anchor=NW, image=un)
            elif bateaux1[y,x]==2:
                window1.create_image(xvoul,yvoul, anchor=NW, image=deux)
            elif bateaux1[y,x]==3:
                window1.create_image(xvoul,yvoul, anchor=NW, image=trois)
            elif bateaux1[y,x]==4:
                window1.create_image(xvoul,yvoul, anchor=NW, image=quatre)
            elif bateaux1[y,x]==5:
                window1.create_image(xvoul,yvoul, anchor=NW, image=cinq)
            elif bateaux1[y,x]==6:
                window1.create_image(xvoul,yvoul, anchor=NW, image=six)
            elif bateaux1[y,x]==7:
                window1.create_image(xvoul,yvoul, anchor=NW, image=sept)
            elif bateaux1[y,x]==8:
                window1.create_image(xvoul,yvoul, anchor=NW, image=huit)


#Detection clic souris

    window1.bind("<Button-1>", pointeurJ1)

#==============================================================================
#window1=Fenetre gauche de jeu
#window2=Fenetre droite de jeu
#window3=Fenetre affichage du bateau a placer
#============================
#gm = mode de jeu
#0=Menu
#1=PvP Tour Joueur 1
#1'=PvP Tour Joueur 2
#2=PvIA
#3=Ecran pour patienter
#4=Placement bateaux + choix
#=============================
#matrice
#0=rien
#1=touche
#2=avant bateau h
#3=milieu bateau h
#4=arriere bateau h
#5=a leau
#6=avant bateau v
#7=milieu bateau v
#8=arriere bateau v
#============================
#Variable jeu
#bateaux1=Matrice J1
#bateaux2=Matrice J2/IA
#============================
#Bateaux:
# 1- 5 cases
# 2- 4 cases
# 3- 3 cases
# 4- 3 cases
# 5- 2 cases
#=============================================================================

Mafenetre = Tk()
Mafenetre.title('Bataille navale')
Mafenetre.geometry('1030x520+200+100')
Mafenetre.resizable(width=False,height=False)
menubar = Menu(Mafenetre)
#barre d'outil
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Menu",command=gm4)
menufichier.add_command(label="Sauvegarder",command=Mafenetre.destroy)
menufichier.add_command(label="Importer",command=Mafenetre.destroy)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Jeu", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Mafenetre.destroy)
menuaide.add_command(label="Regles",command=Mafenetre.destroy)
menubar.add_cascade(label="Aide", menu=menuaide)
#affichage barre d'outil
Mafenetre.config(menu=menubar)
#=============================
#Definition des canevas
Largeur=500
Hauteur=500
window1 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
window1.pack(padx =5, pady =5, side=LEFT)
window2 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
window2.pack(padx =5, pady =5, side=RIGHT)
BoutonJouer = Button(window2, text ='Jouer', command = Mafenetre.destroy)
BoutonImporter = Button(window2, text ='Importer', command = Mafenetre.destroy)
BoutonRegles = Button(window2, text ='Regles', command = Mafenetre.destroy)
BoutonApropos = Button(window2, text ='A propos', command = Mafenetre.destroy)
BoutonQuitter = Button(window2, text ='Quitter', command = Mafenetre.destroy)
#Importation images
#un = PhotoImage(file="")
deux = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/avant.gif")
trois = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/milieu.gif")
quatre = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/arriere.gif")
#cinq = PhotoImage(file="")
six = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/avant1.gif")
sept = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/milieu1.gif")
huit = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/arriere1.gif")
#=============================
#PREMIERE FOIS
imagemenu = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/bg.gif")
photo = PhotoImage(file="C:/Users\Gautier/Documents/GitHub/ISN/EauFond.gif")
gm0()

Mafenetre.mainloop()
