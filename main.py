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
from numpy import *
import tkinter.filedialog
#gm = mode de jeu
#0=Menu
#1=PvP
#2=PvIA
#3=Ecran pour patienter
#4=Placement bateaux + choix
#=============================
#matrice
#0=rien
#1=touché
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
gm=4
Mafenetre = Tk()
Mafenetre.title('Bataille navale')
Mafenetre.geometry('1030x520+200+100')
Mafenetre.resizable(width=False,height=False)
menubar = Menu(Mafenetre)
#barre d'outil
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Menu",command=Mafenetre.destroy)
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
#Menu
if gm==0:
    Largeur = 500
    Hauteur = 500
    menu = Canvas(Mafenetre, width = Largeur, height = Hauteur, bg ='white')
    menu.pack(padx =10, pady =10, side=LEFT)
    image = PhotoImage(file="F:/Bataille-navale-vs-ia/bg.gif")
    menu.create_image(0, 0, image = image, anchor = NW)




if gm==1:
    #Fenetre de jeu
    Largeur = 500
    Hauteur = 500
    photo = PhotoImage(file="F:/Bataille-navale-vs-ia/EauFond.gif")
    window1 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    window1.pack(padx =5, pady =5, side=LEFT)
    window2 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    window2.pack(padx =5, pady =5, side=RIGHT)
    img1 = window1.create_image(50,50,anchor=NW, image=photo)
    img2 = window2.create_image(50,50,anchor=NW, image=photo)

#Fonction détection souris
    def pointeur(event):
        casex=str(event.x)/10
        casey=str(event.y)/10
        if casex > 0 and casey > 0 :
            test=test


#Détection clic souris

    window1.bind("<Button-1>", pointeur)

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

if gm==4:
 #Fenetre de choix
    Largeur = 500
    Hauteur = 500
    photo = PhotoImage(file="F:/Bataille-navale-vs-ia/EauFond.gif")
    window1 = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    window1.pack(padx =5, pady =5, side=LEFT)
    window3 = Canvas(Mafenetre, width = 100, height =Hauteur, bg ='white')
    window3.pack(padx =5, pady =5, side=LEFT)
    photo = PhotoImage(file="F:/Bataille-navale-vs-ia/EauFond.gif")
    img1 = window1.create_image(50,50,anchor=NW, image=photo)
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

#Création matrice
    bateaux1=zeros((9,9))
#Importation images
    #un = PhotoImage(file="")
    deux = PhotoImage(file="F:/Bataille-navale-vs-ia/avant.gif")
    trois = PhotoImage(file="F:/Bataille-navale-vs-ia/milieu.gif")
    quatre = PhotoImage(file="F:/Bataille-navale-vs-ia/arriere.gif")
    #cinq = PhotoImage(file="")
    six = PhotoImage(file="F:/Bataille-navale-vs-ia/avant1.gif")
    sept = PhotoImage(file="F:/Bataille-navale-vs-ia/milieu1.gif")
    huit = PhotoImage(file="F:/Bataille-navale-vs-ia/arriere1.gif")
#Affichage bateau
    for x in range(9):
        for y in range(9):
            xvoul=x*10+50
            yvoul=y*10+50
            if bateaux1[x,y]==1:
                window1.create_image(xvoul,yvoul,anchor=NW, image=un)
            elif bateaux1[x,y]==2:
                window1.create_image(xvoul,yvoul,anchor=NW, image=deux)
            elif bateaux1[x,y]==3:
                window1.create_image(xvoul,yvoul,anchor=NW, image=trois)
            elif bateaux1[x,y]==4:
                window1.create_image(xvoul,yvoul,anchor=NW, image=quatre)
            elif bateaux1[x,y]==5:
                window1.create_image(xvoul,yvoul,anchor=NW, image=cinq)
            elif bateaux1[x,y]==6:
                window1.create_image(xvoul,yvoul,anchor=NW, image=six)
            elif bateaux1[x,y]==7:
                window1.create_image(xvoul,yvoul,anchor=NW, image=sept)
            elif bateaux1[x,y]==8:
                window1.create_image(xvoul,yvoul,anchor=NW, image=huit)

#Fonction détection souris
    def pointeur(event):
        casex=str(event.x)/10
        casey=str(event.y)/10
        if casex > 0 and casey > 0 :
            casex-=1
            casey-=1



#Détection clic souris

    window1.bind("<Button-1>", pointeur)




Mafenetre.mainloop()