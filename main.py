# coding: utf8
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

from random import *
from tkinter import *
from math import *
from numpy import *
import tkinter.filedialog
from tkinter.messagebox import *
import os
#Toutes les fonctions
#===========================
#Affichage bateau
def AffichageBateaux():
    global joueur
    if joueur==1:
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux1[y,x]==0:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux1[y,x]==1:
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
    elif joueur==2:
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux2[y,x]==0:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux2[y,x]==1:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux2[y,x]==2:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=deux)
                elif bateaux2[y,x]==3:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=trois)
                elif bateaux2[y,x]==4:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                elif bateaux2[y,x]==5:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=cinq)
                elif bateaux2[y,x]==6:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=six)
                elif bateaux2[y,x]==7:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=sept)
                elif bateaux2[y,x]==8:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=huit)
#Changer mode horizontal -> vertical + vertical-> horizontal
def Mode():
    global mode
    if mode=="h":
        mode="v"
    else:
        mode="h"
    gm4()
#Joueur vs Joueur
def J2():
    global joueur
    joueur=2
    global bateau
    bateau=1
    BoutonAmi.place_forget()
    BoutonFacile.place_forget()
    BoutonMoyen.place_forget()
    BoutonDifficile.place_forget()
    gm4()

#Pointeur in game J1
def pointeurJeuJ1(event):
    global bateaux2
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    if casex>1 and casey>1 and bateaux2[casey-2,casex-2]!=1 and bateaux2[casey-2,casex-2]!=5:
        window1.unbind('<Button-1>')
        window1.unbind('<Button-3>')
        window1.delete(ALL)
        window2.delete(ALL)
        window1.create_image(0, 0, image = TourJ2, anchor = NW)
        if bateaux2[casey-2,casex-2]==0:
            window1.create_image(250, 450, image = Eau, anchor = CENTER)
            bateaux2[casey-2,casex-2]=5
        elif bateaux2[casey-2,casex-2]==2 or bateaux2[casey-2,casex-2]==3 or bateaux2[casey-2,casex-2]==4 or bateaux2[casey-2,casex-2]==6 or bateaux2[casey-2,casex-2]==7 or bateaux2[casey-2,casex-2]==8:
            window1.create_image(250, 450, image = Touche, anchor = CENTER)
            bateaux2[casey-2,casex-2]=1
        window2.after(1, wait, 5, time_is_up2)

#Pointeur in game J2
def pointeurJeuJ2(event):
    global bateaux1
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    if casex>1 and casey>1 and bateaux1[casey-2,casex-2]!=1 and bateaux1[casey-2,casex-2]!=5:
        window1.unbind('<Button-1>')
        window1.unbind('<Button-3>')
        window1.delete(ALL)
        window2.delete(ALL)
        window1.create_image(0, 0, image = TourJ1, anchor = NW)
        if bateaux1[casey-2,casex-2]==0:
            window1.create_image(250, 450, image = Eau, anchor = CENTER)
            bateaux1[casey-2,casex-2]=5
        elif bateaux1[casey-2,casex-2]==2 or bateaux1[casey-2,casex-2]==3 or bateaux1[casey-2,casex-2]==4 or bateaux1[casey-2,casex-2]==6 or bateaux1[casey-2,casex-2]==7 or bateaux1[casey-2,casex-2]==8:
            window1.create_image(250, 450, image = Touche, anchor = CENTER)
            bateaux1[casey-2,casex-2]=1
        window2.after(1, wait, 5, time_is_up1)

#Detection souris J1
def pointeurJ1(event):
    global bateaux1
    global bateau
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    limite=0
    colision=0
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
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==2:
                if casex<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0 and bateaux1[casey-2,casex+1]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=3
                        bateaux1[casey-2,casex+1]=4
                        bateau=3
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==3:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=4
                        bateau=4
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==4:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=3
                        bateaux1[casey-2,casex]=4
                        bateau=5
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==5:
                if casex<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0:
                        bateaux1[casey-2,casex-2]=2
                        bateaux1[casey-2,casex-1]=4
                        BoutonAmi.place(relx = 0.6, rely =0.1, anchor = E)
                        BoutonFacile.place(relx = 0.6, rely =0.3, anchor = E)
                        BoutonMoyen.place(relx = 0.6, rely =0.5, anchor = E)
                        BoutonDifficile.place(relx = 0.6, rely =0.7, anchor = E)
                        bateau=10
                    else:
                        colision=1
                else:
                    limite=1

#MODE VERTICAL
        elif mode=="v":
            if bateau==1:
                if casey<7:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0 and bateaux1[casey+2,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=7
                        bateaux1[casey+1,casex-2]=7
                        bateaux1[casey+2,casex-2]=8
                        bateau=2
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==2:
                if casey<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=7
                        bateaux1[casey+1,casex-2]=8
                        bateau=3
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==3:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=8
                        bateau=4
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==4:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=8
                        bateau=5
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==5:
                if casey<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=8
                        BoutonAmi.place(relx = 0.6, rely =0.1, anchor = E)
                        BoutonFacile.place(relx = 0.6, rely =0.3, anchor = E)
                        BoutonMoyen.place(relx = 0.6, rely =0.5, anchor = E)
                        BoutonDifficile.place(relx = 0.6, rely =0.7, anchor = E)
                        bateau=10
                    else:
                        colision=1
                else:
                    limite=1

        if limite==1:
            showerror('Erreur', 'Votre bateau sors des limites')
        if colision==1:
            showerror('Erreur', 'Votre bateau entre en colision avec un autre')
        gm4()
    else:
        showerror('Erreur', 'Vous n\'êtes pas sur le plateau de jeu')

#Detection souris J2
def pointeurJ2(event):
    global bateaux2
    global bateau
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    limite=0
    colision=0
    if casex>1 and casey>1:
#MODE HORIZONTAL
        if mode=="h":
            if bateau==1:
                if casex<7:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0 and bateaux2[casey-2,casex+2]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=3
                        bateaux2[casey-2,casex+1]=3
                        bateaux2[casey-2,casex+2]=4
                        bateau=2
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==2:
                if casex<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=3
                        bateaux2[casey-2,casex+1]=4
                        bateau=3
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==3:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=4
                        bateau=4
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==4:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=4
                        bateau=5
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==5:
                if casex<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=4
                        bateau=0
                    else:
                        colision=1
                else:
                    limite=1


#MODE VERTICAL
        elif mode=="v":
            if bateau==1:
                if casey<7:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0 and bateaux2[casey+1,casex-2]==0 and bateaux2[casey+2,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=7
                        bateaux2[casey+1,casex-2]=7
                        bateaux2[casey+2,casex-2]=8
                        bateau=2
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==2:
                if casey<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0 and bateaux2[casey+1,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=7
                        bateaux2[casey+1,casex-2]=8
                        bateau=3
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==3:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=8
                        bateau=4
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==4:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=8
                        bateau=5
                    else:
                        colision=1
                else:
                    limite=1

            elif bateau==5:
                if casey<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=8
                        bateau=0
                    else:
                        colision=1
                else:
                    limite=1

        if limite==1:
            showerror('Erreur', 'Votre bateau sors des limites')
        if colision==1:
            showerror('Erreur', 'Votre bateau entre en colision avec un autre')

        if bateau==0:
            reset_affichage()
            window1.create_image(0, 0, image = TourJ1, anchor = NW)
            window2.after(1, wait, 5, time_is_up1)
        else:
            gm4()

    else:
        showerror('Erreur', 'Vous n\'êtes pas sur le plateau de jeu')
def imagebateau1(event):
    global bateaux1
    global bateau
    gm4()
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    if casex>1 and casey>1:
        xvoul=casex*50-50
        yvoul=casey*50-50

#MODE HORIZONTAL
        if mode=="h":
            if bateau==1:
                if casex<7:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0 and bateaux1[casey-2,casex+1]==0 and bateaux1[casey-2,casex+2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+150,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+200,yvoul,image=Ghost,anchor=NW)
            elif bateau==2:
                if casex<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0 and bateaux1[casey-2,casex+1]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+150,yvoul,image=Ghost,anchor=NW)
            elif bateau==3:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
            elif bateau==4:
                if casex<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0 and bateaux1[casey-2,casex]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
            elif bateau==5:
                if casex<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-2,casex-1]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
#MODE VERTICAL
        elif mode=="v":
            if bateau==1:
                if casey<7:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0 and bateaux1[casey+2,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+150,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+200,image=Ghost,anchor=NW)
            elif bateau==2:
                if casey<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+150,image=Ghost,anchor=NW)
            elif bateau==3:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
            elif bateau==4:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
            elif bateau==5:
                if casey<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
    lignes1()
#Images bateau J2
def imagebateau2(event):
    global bateaux2
    global bateau
    gm4()
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    if casex>1 and casey>1:
        xvoul=casex*50-50
        yvoul=casey*50-50

#MODE HORIZONTAL
        if mode=="h":
            if bateau==1:
                if casex<7:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0 and bateaux2[casey-2,casex+2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+150,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+200,yvoul,image=Ghost,anchor=NW)
            elif bateau==2:
                if casex<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+150,yvoul,image=Ghost,anchor=NW)
            elif bateau==3:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
            elif bateau==4:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+100,yvoul,image=Ghost,anchor=NW)
            elif bateau==5:
                if casex<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul+50,yvoul,image=Ghost,anchor=NW)
#MODE VERTICAL
        elif mode=="v":
            if bateau==1:
                if casey<7:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0 and bateaux2[casey+1,casex-2]==0 and bateaux2[casey+2,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+150,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+200,image=Ghost,anchor=NW)
            elif bateau==2:
                if casey<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0 and bateaux2[casey+1,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+150,image=Ghost,anchor=NW)
            elif bateau==3:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
            elif bateau==4:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+100,image=Ghost,anchor=NW)
            elif bateau==5:
                if casey<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0:
                        window1.create_image(xvoul,yvoul,image=Ghost,anchor=NW)
                        window1.create_image(xvoul,yvoul+50,image=Ghost,anchor=NW)
    lignes1()
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
def lignes2():
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

def IA(degre):
    reset_affichage()
    global bateau
    global difficulty
    global bateaux2
    bateau=1
    difficulty=degre
    bateaux2=zeros((9,9))
#Génération matrice du bateau
#bateau1
    while bateau==1:
        x=random.choice([0,1,2,3,4,5,6,7,8])
        y=random.choice([0,1,2,3,4,5,6,7,8])
        mode=random.choice(["h","v"])
        if mode=="h":
            if x<5:
                    if bateaux2[y,x]==0 and bateaux2[y,x+1]==0 and bateaux2[y,x+2]==0 and bateaux2[y,x+3]==0 and bateaux2[y,x+4]==0:
                        bateaux2[y,x]=2
                        bateaux2[y,x+1]=3
                        bateaux2[y,x+2]=3
                        bateaux2[y,x+3]=3
                        bateaux2[y,x+4]=4
                        bateau=2
        elif mode=="v":
            if y<5:
                    if bateaux2[y,x]==0 and bateaux2[y+1,x]==0 and bateaux2[y+2,x]==0 and bateaux2[y+3,x]==0 and bateaux2[y+4,x]==0:
                        bateaux2[y,x]=6
                        bateaux2[y+1,x]=7
                        bateaux2[y+2,x]=7
                        bateaux2[y+3,x]=7
                        bateaux2[y+4,x]=8
                        bateau=2
#bateau2
    while bateau==2:
        x=random.choice([0,1,2,3,4,5,6,7,8])
        y=random.choice([0,1,2,3,4,5,6,7,8])
        mode=random.choice(["h","v"])
        if mode=="h":
            if x<6:
                    if bateaux2[y,x]==0 and bateaux2[y,x+1]==0 and bateaux2[y,x+2]==0 and bateaux2[y,x+3]==0:
                        bateaux2[y,x]=2
                        bateaux2[y,x+1]=3
                        bateaux2[y,x+2]=3
                        bateaux2[y,x+3]=4
                        bateau=3
        elif mode=="v":
            if y<6:
                    if bateaux2[y,x]==0 and bateaux2[y+1,x]==0 and bateaux2[y+2,x]==0 and bateaux2[y+3,x]==0:
                        bateaux2[y,x]=6
                        bateaux2[y+1,x]=7
                        bateaux2[y+2,x]=7
                        bateaux2[y+3,x]=8
                        bateau=3
#bateau3+4
    while bateau==3 or bateau==4:
        x=random.choice([0,1,2,3,4,5,6,7,8])
        y=random.choice([0,1,2,3,4,5,6,7,8])
        mode=random.choice(["h","v"])
        if mode=="h":
            if x<7:
                    if bateaux2[y,x]==0 and bateaux2[y,x+1]==0 and bateaux2[y,x+2]==0:
                        bateaux2[y,x]=2
                        bateaux2[y,x+1]=3
                        bateaux2[y,x+2]=4
                        bateau+=1
        elif mode=="v":
            if y<7:
                    if bateaux2[y,x]==0 and bateaux2[y+1,x]==0 and bateaux2[y+2,x]==0:
                        bateaux2[y,x]=6
                        bateaux2[y+1,x]=7
                        bateaux2[y+2,x]=8
                        bateau+=1
#bateau5
    while bateau==5:
        x=random.choice([0,1,2,3,4,5,6,7,8])
        y=random.choice([0,1,2,3,4,5,6,7,8])
        mode=random.choice(["h","v"])
        if mode=="h":
            if x<8:
                    if bateaux2[y,x]==0 and bateaux2[y,x+1]==0:
                        bateaux2[y,x]=2
                        bateaux2[y,x+1]=4
                        bateau=10
        elif mode=="v":
            if y<8:
                    if bateaux2[y,x]==0 and bateaux2[y+1,x]==0:
                        bateaux2[y,x]=6
                        bateaux2[y+1,x]=8
                        bateau=10
    gm2()
#=================================================================================
# PointeurIAJ1
# Variables:
# bateaux1: Matrice bateau 1
# bateaux2: Matrice bateau 2
# difficulty: difficultée de l'IA
# xt: coordonnées bateau touché en x
# yt: coordonnées bateau touché en y
# x1: vérification plus de bateau sur la gauche
# x2: vérification plus de bateau sur la droite
# y1: vérification plus de bateau vers le haut
# y2: vérification plus de bateau vers le bas
# xy: retirer si la case que l'on s'apprête a tester est déjà touchée/à l'eau
# IsShotNear: IA difficultée difficile: Vérifie si il ne tire pas inutilement
#=================================================================================
def pointeurIAJ1(event):
    global bateaux1
    global bateaux2
    global difficulty
    global xt,yt,x1,x2,y1,y2
    xy=0
#Gestion du tir du joueur
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    if casex>1 and casey>1 and bateaux2[casey-2,casex-2]!=1 and bateaux2[casey-2,casex-2]!=5:
#On prépare la fenêtre d'attente
        window1.unbind('<Button-1>')
        window1.unbind('<Button-3>')
        window1.delete(ALL)
        window2.delete(ALL)
        window1.create_image(0, 0, image = IAimage, anchor = NW)
        if bateaux2[casey-2,casex-2]==0:
            window1.create_image(300, 45, image = Eau, anchor = CENTER)
            bateaux2[casey-2,casex-2]=5
        elif bateaux2[casey-2,casex-2]==2 or bateaux2[casey-2,casex-2]==3 or bateaux2[casey-2,casex-2]==4 or bateaux2[casey-2,casex-2]==6 or bateaux2[casey-2,casex-2]==7 or bateaux2[casey-2,casex-2]==8:
            window1.create_image(300, 45, image = Touche, anchor = CENTER)
            bateaux2[casey-2,casex-2]=1
#==============================PARTIE IA===========================================
#Tir aléatoire
        FindNothing=1
        while FindNothing==1:
            x=random.choice([0,1,2,3,4,5,6,7,8])
            y=random.choice([0,1,2,3,4,5,6,7,8])
            if bateaux1[y,x]!=1 and bateaux1[y,x]!=5:
                FindNothing=0
#Si difficultée est difficile + on a pas touché de bateaux, on vérifie où l'on tir
        if difficulty==3 and xt==10 and yt==10:
            IsShotNear=5
#Tant qu'il y a 4 cases à l'eau autour
            while IsShotNear>3:
                IsShotNear=0
                if x<=7:
                    if bateaux1[x+1,y]==5:
                        IsShotNear+=1
                if x>=1:
                    if bateaux1[x-1,y]==5:
                        IsShotNear+=1
                if y<=7:
                    if bateaux1[x,y+1]==5:
                        IsShotNear+=1
                if y>=1:
                    if bateaux1[x,y-1]==5:
                        IsShotNear+=1
                if IsShotNear>3:
#On change le x et le y si trop de cases à l'eau autour
                    x=random.choice([0,1,2,3,4,5,6,7,8])
                    y=random.choice([0,1,2,3,4,5,6,7,8])
                else:
#Si c'est une case touchée ou à l'eau on recommence
                    if bateaux1[y,x]==5 or bateaux1[y,x]==1:
                        IsShotNear=5
#Si difficultée est moyen ou difficile et qu'un bateau à été touché, on traque ce bateau
        if difficulty>=2:
            if xt!=10 and yt!=10:
#Vérification vers la gauche
                if x1==0:
                    x=xt
                    y=yt
                    FindNoFire=1
#On va vers la gauche en partant de la case de départ jusqu'à une case non touchée
                    while FindNoFire==1:
                        x-=1
                        if x<0 or bateaux1[y,x]==5:
                            FindNoFire=0
                            x1=1
                            xy=1
                        else:
                            if bateaux1[y,x]!=1:
                                FindNoFire=0
                    if x>=0:
                        if difficulty==3:
                            if bateaux1[y,x]==2:
                                x1=1
                        if bateaux1[y,x]==0:
                            x1=1
#Vérification vers la droite
                elif x2==0:
                    x=xt
                    y=yt
                    FindNoFire=1
#On va vers la droite en partant de la case de départ jusqu'à une case non touchée
                    while FindNoFire==1:
                        x+=1
                        if x>8 or bateaux1[y,x]==5:
                            FindNoFire=0
                            x2=1
                            xy=1
                        else:
                            if bateaux1[y,x]!=1:
                                FindNoFire=0
                    if x<=8:
                        if difficulty==3:
                            if bateaux1[y,x]==4:
                                x2=1
                        if bateaux1[y,x]==0:
                            x2=1
#Vérification vers le haut
                elif y1==0:
                    x=xt
                    y=yt
                    FindNoFire=1
#On va vers le haut en partant de la case de départ jusqu'à une case non touchée
                    while FindNoFire==1:
                        y-=1
                        if y<0 or bateaux1[y,x]==5:
                            FindNoFire=0
                            y1=1
                            xy=1
                        else:
                            if bateaux1[y,x]!=1:
                                FindNoFire=0
                    if y>=0:
                        if difficulty==3:
                            if bateaux1[y,x]==6:
                                y1=1
                        if bateaux1[y,x]==0:
                            y1=1
#Vérification vers le bas
                elif y2==0:
                    x=xt
                    y=yt
                    FindNoFire=1
#On va vers le bas en partant de la case de départ jusqu'à une case non touchée
                    while FindNoFire==1:
                        y+=1
                        if y>8 or bateaux1[y,x]==5:
                            FindNoFire=0
                            y2=1
                            xy=1
                        else:
                            if bateaux1[y,x]!=1:
                                FindNoFire=0
                    if y<=8:
                        if difficulty==3:
                            if bateaux1[y,x]==8:
                                y2=1
                        if bateaux1[y,x]==0:
                            y2=1
#Je reset les variables de l'IA si j'ai fini de vérifier
                if y2==1:
                    xt=10
                    yt=10
                    x1=0
                    x2=0
                    y1=0
                    y2=0
#Si je dois tirer aléatoiremenet car soucis (Voir en haut)
        if xy==1:
#On ne tire pas aléatoirement si difficultée difficile
            if difficulty==3 and xt==10 and yt==10:
                IsShotNear=5
                while IsShotNear>3:
                    IsShotNear=0
                    if x<=7:
                        if bateaux1[x+1,y]==5:
                            IsShotNear+=1
                    if x>=1:
                        if bateaux1[x-1,y]==5:
                            IsShotNear+=1
                    if y<=7:
                        if bateaux1[x,y+1]==5:
                            IsShotNear+=1
                    if y>=1:
                        if bateaux1[x,y-1]==5:
                            IsShotNear+=1
                    if IsShotNear>3:
                        x=random.choice([0,1,2,3,4,5,6,7,8])
                        y=random.choice([0,1,2,3,4,5,6,7,8])
                    elif bateaux1[y,x]==5 or bateaux1[y,x]==1:
                        IsShotNear=5
                        x=random.choice([0,1,2,3,4,5,6,7,8])
                        y=random.choice([0,1,2,3,4,5,6,7,8])
#Sinon on tire aléatoirement
            else:
                FindNothing=1
                while FindNothing==1:
                    x=random.choice([0,1,2,3,4,5,6,7,8])
                    y=random.choice([0,1,2,3,4,5,6,7,8])
                    if bateaux1[y,x]!=1 and bateaux1[y,x]!=5:
                        FindNothing=0

#On regarde la ou on a tirer
        if bateaux1[y,x]==2 or bateaux1[y,x]==3 or bateaux1[y,x]==4 or bateaux1[y,x]==6 or bateaux1[y,x]==7 or bateaux1[y,x]==8:
            bateaux1[y,x]=1
            if difficulty==2 or difficulty ==3:
                if xt==10 and yt==10:
#On le rentre dans une variable si on est pas déjà en train de traquer un bateau
                    xt=x
                    yt=y
            window1.create_image(300, 440, image = Touche, anchor = CENTER)
        elif bateaux1[y,x]==0:
            bateaux1[y,x]=5
            window1.create_image(300, 440, image = Eau, anchor = CENTER)
#On attend 2 secondes
        window2.after(1, wait, 2, gm2)


def pointeurMenu(event):
    if event.x>28 and event.y>365 and event.y<415 and event.x<173:
        gm6()
    elif event.x>28 and event.y<470 and event.y>415 and event.x<173:
        gm5(2)
    elif event.x>330 and event.y>365 and event.y<415 and event.x<480:
        print("ok pour importer")
    elif event.x>330 and event.y>415 and event.y<470 and event.x<480:
        Mafenetre.destroy()
    elif (event.x>200 and event.x<305 and event.y>374 and event.y<452) or (event.x>188 and event.x<315 and event.y>395 and event.y<439) or (event.x>223 and event.x<280 and event.y>374 and event.y<468):
        gm4()

def pointeurImporter(event):
    global bateau,joueur,bateaux1,bateaux2
    if event.y<166:
        if askyesno("Sauvegarde 1","Êtes vous sur de vouloir importer la partie du slot 1 ?")==True:
            fichier1 = open("saves/save1.txt", "r")
            bateaux1=zeros((9,9))
            bateaux2=zeros((9,9))
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier1.read(1)
                    bateaux1[y,x]=char
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier1.read(1)
                    bateaux2[y,x]=char
            joueur=fichier1.read(1)
            fichier1.close()
    elif event.y>=166 and event.y<=332:
        if askyesno("Sauvegarde 2","Êtes vous sur de vouloir importer la partie du slot 2 ?")==True:
            fichier2 = open("saves/save2.txt", "r")
            bateaux1=zeros((9,9))
            bateaux2=zeros((9,9))
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier2.read(1)
                    bateaux1[y,x]=char
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier2.read(1)
                    bateaux2[y,x]=char
            joueur=fichier2.read(1)
            fichier2.close()
    elif event.y>332:
        if askyesno("Sauvegarde 3","Êtes vous sur de vouloir importer la partie du slot 3 ?")==True:
            fichier3 = open("saves/save3.txt", "r")
            bateaux1=zeros((9,9))
            bateaux2=zeros((9,9))
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier3.read(1)
                    bateaux1[y,x]=char
            for y in range(0,9):
                for x in range(0,9):
                    char = fichier3.read(1)
                    bateaux2[y,x]=char
            joueur=fichier3.read(1)
            fichier3.close()
    reset_affichage()
    if joueur=="1":
        window1.create_image(0, 0, image = TourJ1, anchor = NW)
        window2.after(1, wait, 3, time_is_up1)
    elif joueur=="2":
        window1.create_image(0, 0, image = TourJ2, anchor = NW)
        window2.after(1, wait, 3, time_is_up2)
    else:
        showerror("Erreur","Erreur lors de l'importation de la partie")
        reset()

def pointeurSave(event):
    global bateau
    global bateaux1
    global bateaux2
    if bateau==0:
        if event.y<166:
            if askyesno("Sauvegarde 1","Êtes vous sur de vouloir sauvegarder la partie dans le slot 1 ?")==True:
                fichier1 = open("saves/save1.txt", "w")
                for y in range(0,9):
                    for x in range(0,9):
                        fichier1.write('%01d' % bateaux1[y,x])
                for y in range(0,9):
                    for x in range(0,9):
                        fichier1.write('%01d' % bateaux2[y,x])
                fichier1.write(str(joueur))
                fichier1.close()
        elif event.y>=166 and event.y<=332:
            if askyesno("Sauvegarde 2","Êtes vous sur de vouloir sauvegarder la partie dans le slot 2 ?")==True:
                fichier2 = open("saves/save2.txt", "w")
                for y in range(0,9):
                    for x in range(0,9):
                        fichier2.write('%01d' % bateaux1[y,x])
                for y in range(0,9):
                    for x in range(0,9):
                        fichier2.write('%01d' % bateaux2[y,x])
                fichier2.write(str(joueur))
                fichier2.close()
        elif event.y>332:
            if askyesno("Sauvegarde 3","Êtes vous sur de vouloir sauvegarder la partie dans le slot 3 ?")==True:
                fichier3 = open("saves/save3.txt", "w")
                for y in range(0,9):
                    for x in range(0,9):
                        fichier3.write('%01d' % bateaux1[y,x])
                for y in range(0,9):
                    for x in range(0,9):
                        fichier3.write('%01d' % bateaux2[y,x])
                fichier3.write(str(joueur))
                fichier3.close()
    else:
        showerror("Erreur","Une erreur s'est produite vous ne pouvez pas enregistrer cette partie.")
        reset()
    #Changer gamemode -> 0
def gm0():
    reset_affichage()
    #MENU
    window1.create_image(0, 0, image = imagemenu, anchor = NW)
    window2.create_image(0, 0, image = imagemenu2, anchor = NW)
    window2.bind("<Button-1>", pointeurMenu)

#============================================================================
#Changer gamemode -> 1
def gm1():
    reset_affichage()
    global joueur
    global bateaux1

    IsBoatLeft=0
    if joueur==1:
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux1[y,x]==0:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux1[y,x]==1:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux1[y,x]==2:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=deux)
                    IsBoatLeft+=1
                elif bateaux1[y,x]==3:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=trois)
                    IsBoatLeft+=1
                elif bateaux1[y,x]==4:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                    IsBoatLeft+=1
                elif bateaux1[y,x]==5:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=cinq)
                elif bateaux1[y,x]==6:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=six)
                    IsBoatLeft+=1
                elif bateaux1[y,x]==7:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=sept)
                    IsBoatLeft+=1
                elif bateaux1[y,x]==8:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=huit)
                    IsBoatLeft+=1
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux2[y,x]==0 or bateaux2[y,x]==2  or bateaux2[y,x]==3 or bateaux2[y,x]==4 or bateaux2[y,x]==6 or bateaux2[y,x]==7 or bateaux2[y,x]==8:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux2[y,x]==1:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux2[y,x]==5:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=cinq)
    elif joueur==2:
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux2[y,x]==0:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux2[y,x]==1:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux2[y,x]==2:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=deux)
                    IsBoatLeft+=1
                elif bateaux2[y,x]==3:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=trois)
                    IsBoatLeft+=1
                elif bateaux2[y,x]==4:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                    IsBoatLeft+=1
                elif bateaux2[y,x]==5:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=cinq)
                elif bateaux2[y,x]==6:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=six)
                    IsBoatLeft+=1
                elif bateaux2[y,x]==7:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=sept)
                    IsBoatLeft+=1
                elif bateaux2[y,x]==8:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=huit)
                    IsBoatLeft+=1
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux1[y,x]==0 or bateaux1[y,x]==2  or bateaux1[y,x]==3 or bateaux1[y,x]==4 or bateaux1[y,x]==6 or bateaux1[y,x]==7 or bateaux1[y,x]==8:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux1[y,x]==1:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux1[y,x]==5:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=cinq)
#Lignes window1
    lignes1()
#Lignes window2
    lignes2()

    if IsBoatLeft==0:
        if joueur==1:
#J2WIN
            window1.unbind('<Button-1>')
            window1.unbind('<Button-3>')
            window1.delete(ALL)
            window2.delete(ALL)
            window1.create_image(0, 0, image = J2WIN, anchor = NW)
            window2.after(1, wait, 5, reset)
        else:
#J1WIN
            window1.unbind('<Button-1>')
            window1.unbind('<Button-3>')
            window1.delete(ALL)
            window2.delete(ALL)
            window1.create_image(0, 0, image = J1WIN, anchor = NW)
            window2.after(1, wait, 5, reset)
    else:
#Detection clic souris
        if joueur==1:
            window1.bind("<Button-1>", pointeurJeuJ1)
        elif joueur==2:
            window1.bind("<Button-1>", pointeurJeuJ2)
#============================================================================
#Changer gamemode -> 2
def gm2():

    global xt
    try:
        xt
    except NameError:
        xt=10

    global yt
    try:
        yt
    except NameError:
        yt=10

    global x1
    try:
        x1
    except NameError:
        x1=0

    global x2
    try:
        x2
    except NameError:
        x2=0

    global y1
    try:
        y1
    except NameError:
        y1=0

    global y2
    try:
        y2
    except NameError:
        y2=0

    reset_affichage()
    IsBoatLeftJ1=0
    IsBoatLeftIA=0

    for x in range(0,9):
        for y in range(0,9):
            xvoul=x*50+50
            yvoul=y*50+50
            if bateaux1[y,x]==0:
                window2.create_image(xvoul,yvoul, anchor=NW, image=zero)
            elif bateaux1[y,x]==1:
                window2.create_image(xvoul,yvoul, anchor=NW, image=un)
            elif bateaux1[y,x]==2:
                window2.create_image(xvoul,yvoul, anchor=NW, image=deux)
                IsBoatLeftJ1+=1
            elif bateaux1[y,x]==3:
                window2.create_image(xvoul,yvoul, anchor=NW, image=trois)
                IsBoatLeftJ1+=1
            elif bateaux1[y,x]==4:
                window2.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                IsBoatLeftJ1+=1
            elif bateaux1[y,x]==5:
                window2.create_image(xvoul,yvoul, anchor=NW, image=cinq)
            elif bateaux1[y,x]==6:
                window2.create_image(xvoul,yvoul, anchor=NW, image=six)
                IsBoatLeftJ1+=1
            elif bateaux1[y,x]==7:
                window2.create_image(xvoul,yvoul, anchor=NW, image=sept)
                IsBoatLeftJ1+=1
            elif bateaux1[y,x]==8:
                window2.create_image(xvoul,yvoul, anchor=NW, image=huit)
                IsBoatLeftJ1+=1
        for x in range(0,9):
            for y in range(0,9):
                xvoul=x*50+50
                yvoul=y*50+50
                if bateaux2[y,x]==0:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                elif bateaux2[y,x]==2  or bateaux2[y,x]==3 or bateaux2[y,x]==4 or bateaux2[y,x]==6 or bateaux2[y,x]==7 or bateaux2[y,x]==8:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=zero)
                    IsBoatLeftIA+=1
                elif bateaux2[y,x]==1:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=un)
                elif bateaux2[y,x]==5:
                    window1.create_image(xvoul,yvoul, anchor=NW, image=cinq)

    lignes1()
    lignes2()

    window1.bind("<Button-1>", pointeurIAJ1)

    if IsBoatLeftIA==0:
#IAWIN
        window1.unbind('<Button-1>')
        window1.unbind('<Button-3>')
        window1.delete(ALL)
        window2.delete(ALL)
        window1.create_image(0, 0, image = J1WIN, anchor = NW)
        window2.after(1, wait, 5, reset)

    elif IsBoatLeftJ1==0:
#J1WIN
        window1.unbind('<Button-1>')
        window1.unbind('<Button-3>')
        window1.delete(ALL)
        window2.delete(ALL)
        window1.create_image(0, 0, image = IAWIN, anchor = NW)
        window2.after(1, wait, 5, reset)
#============================================================================
#Changer gamemode -> 3
def gm3():
    global bateaux1
    global bateaux2
    Test=0
    try:
        bateaux1
    except NameError:
        Test+=1
    try:
        bateaux2
    except NameError:
        Test+=1

    if Test==0:
        reset_affichage()
        window1.create_image(0, 0, image = SaveFond, anchor = NW)
        window2.create_image(0, 0, image = Save, anchor = NW)
        window1.bind("<Button-1>", pointeurSave)
    else:
        reset()

#============================================================================
#Changer gamemode -> 4
def gm4():
    window1.unbind('<Button-1>')
    window1.unbind('<Button-3>')
    window2.unbind('<Button-1>')
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
    window2.create_image(0, 0, image = Instruc, anchor = NW)
    if bateau==1:
        if mode=="h":
            window2.create_image(0, 0, image = CinqH, anchor = NW)
        elif mode=="v":
            window2.create_image(0, 0, image = CinqV, anchor = NW)
    elif bateau==2:
        if mode=="h":
            window2.create_image(0, 0, image = QuatreH, anchor = NW)
        elif mode=="v":
            window2.create_image(0, 0, image = QuatreV, anchor = NW)
    elif bateau==3 or bateau==4:
        if mode=="h":
            window2.create_image(0, 0, image = TroisH, anchor = NW)
        elif mode=="v":
            window2.create_image(0, 0, image = TroisV, anchor = NW)
    elif bateau==5:
        if mode=="h":
            window2.create_image(0, 0, image = DeuxH, anchor = NW)
        elif mode=="v":
            window2.create_image(0, 0, image = DeuxV, anchor = NW)
#Creation matrice
    global bateaux1
    try:
        bateaux1
    except NameError:
        bateaux1=zeros((9,9))

    global bateaux2
    try:
        bateaux2
    except NameError:
        bateaux2=zeros((9,9))

    BoutonMode.place(relx = 0.8, rely =0.8, anchor = E)

    AffichageBateaux()

    lignes1()

#Detection clic souris
    if joueur==1:
        window1.bind("<Button-1>", pointeurJ1)
        window1.bind('<Button-3>', imagebateau1)
    elif joueur==2:
        window1.bind("<Button-1>", pointeurJ2)
        window1.bind('<Button-3>', imagebateau2)

#============================================================================
#Changer gamemode -> 5
def gm5(pageRF):
    Boutonsuivant.place_forget()
    Boutonprec.place_forget()
    global pageR
    if pageRF==4:
        pageR-=1
    elif pageRF==3:
        pageR+=1
    else:
        page=1
    Test=0
    global bateaux1
    try:
        bateaux1
    except NameError:
        Test=1
    else:
        if askyesno("Règles","Êtes vous sur de vouloir accéder aux règles ? Votre partie sera effacée.")==True:
            Test=1
    if Test==1:
        reset_affichage()
        if pageR==1:
            window1.create_image( 0, 0, image = regle1, anchor = NW)
            window2.create_image(0, 0, image = regle2, anchor = NW)
            Boutonsuivant.place(relx = 0.89, rely =0.94, anchor = NW)
        elif pageR==2:
            window1.create_image( 0, 0, image = regle3, anchor = NW)
            Boutonprec.place(relx =0.87, rely =0.94, anchor = NW)
#============================================================================
#Changer gamemode -> 6
def gm6():
    global bateaux1
    global bateaux2
    Test=0
    try:
        bateaux1
    except NameError:
        Test+=1
    else:
        if askyesno("","Êtes vous sur de vouloir importer une partie ?")==True:
            Test+=1
    if Test!=0:
        reset()
        reset_affichage()
        window1.create_image(0, 0, image = SaveFond, anchor = NW)
        window2.create_image(0, 0, image = Import, anchor = NW)
        window1.bind("<Button-1>", pointeurImporter)

#Temps d'attente
def wait(remaining_time, callback):
    if remaining_time==5:
        window2.create_image(10, 10, image = Restant5, anchor = NW)
    elif remaining_time==4:
        window2.create_image(10, 10, image = Restant4, anchor = NW)
    elif remaining_time==3:
        window2.create_image(10, 10, image = Restant3, anchor = NW)
    elif remaining_time==2:
        window2.create_image(10, 10, image = Restant2, anchor = NW)
    elif remaining_time==1:
        window2.create_image(10, 10, image = Restant1, anchor = NW)
    if remaining_time > 0:
        remaining_time -= 1
        window2.after(1000, wait, remaining_time, callback)
    else:
        callback()

def time_is_up1():
#Une fois le temps ecoule
    global joueur
    joueur=1
    gm1()

def time_is_up2():
#Une fois le temps ecoule
    global joueur
    joueur=2
    gm1()

#Reset boutons
def reset_affichage():

    BoutonAmi.place_forget()
    BoutonMode.place_forget()
    BoutonFacile.place_forget()
    BoutonMoyen.place_forget()
    BoutonDifficile.place_forget()
    Boutonsuivant.place_forget()
    Boutonprec.place_forget()

    window1.unbind('<Button-1>')
    window1.unbind('<Button-3>')
    window2.unbind('<Button-1>')

    window1.delete(ALL)
    window2.delete(ALL)
#Reset
def reset():

    reset_affichage()

    global joueur,bateaux1,bateaux2,bateau,mode,difficulty,xt,yt,x1,x2,y1,y2
#Variable x touché
    try:
        xt
    except NameError:
        print("")
    else:
        del xt
#Variable y touché
    try:
        yt
    except NameError:
        print("")
    else:
        del yt
#Variable difficultee
    try:
        x1
    except NameError:
        print("")
    else:
        del x1
#Variable difficultee
    try:
        x2
    except NameError:
        print("")
    else:
        del x2
#Variable difficultee
    try:
        y1
    except NameError:
        print("")
    else:
        del y1
#Variable difficultee
    try:
        y2
    except NameError:
        print("")
    else:
        del y2
#Variable difficultee
    try:
        difficulty
    except NameError:
        print("")
    else:
        del difficulty
#Variable joueur
    try:
        joueur
    except NameError:
        print("")
    else:
        del joueur
#Matrice bateaux1+2
    try:
        bateaux1
    except NameError:
        print("")
    else:
        del bateaux1

    try:
        bateaux2
    except NameError:
        print("")
    else:
        del bateaux2
#Variable bateau
    try:
        bateau
    except NameError:
        print("")
    else:
        del bateau
#Mode
    mode="h"

    gm0()
#==============================================================================
#intelligence artificielle
#xt=x touché
#yt=y touché
#x1=verif vers la gauche
#x2=verif vers la droite
#y1=verif vers le haut
#y2=verif vers le bas
#xy=relancer la roulette
#============================
#mode:
#h= horizontal
#v= vertical
#============================
#window1=Fenetre gauche de jeu
#window2=Fenetre droite de jeu
#============================
#gm = mode de jeu
#0=Menu
#1=PvP Tour Joueur 1
#1'=PvP Tour Joueur 2
#2=PvIA
#3=Sauvegarder
#4=Placement bateaux + choix
#=============================
#wait
#TourJ1 = Image tour du J1
#TourJ2 = Image tour du J2
#Restant5 = Image 5
#Restant4 = Image 4
#Restant3 = Image 3
#Restant2 = Image 2
#Restant1 = Image 1
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
#Difficulty
#1=facile
#2=moyen
#3=difficile
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
menufichier.add_command(label="Menu",command=reset)
menufichier.add_command(label="Sauvegarder",command=gm3)
menufichier.add_command(label="Importer",command=gm6)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Jeu", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Mafenetre.destroy)
menuaide.add_command(label="Règles",command= lambda : gm5(2))
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
#Wait
Touche = PhotoImage(file="img/texte1.gif")
Eau = PhotoImage(file="img/texte2.gif")
TourJ1 = PhotoImage(file="img/J1.gif")
TourJ2 = PhotoImage(file="img/J2.gif")
Restant5 = PhotoImage(file="img/5.gif")
Restant4 = PhotoImage(file="img/4.gif")
Restant3 = PhotoImage(file="img/3.gif")
Restant2 = PhotoImage(file="img/2.gif")
Restant1 = PhotoImage(file="img/1.gif")
#Ghost
Ghost = PhotoImage(file="img/ghost.gif")
#Mode de display
mode="h"
#IA
IAimage = PhotoImage(file="img/IA.gif")
#WIN
IAWIN = PhotoImage(file="img/IAWIN.gif")
J1WIN = PhotoImage(file="img/J1WIN.gif")
J2WIN = PhotoImage(file="img/J2WIN.gif")
#bateaux en entier
CinqH = PhotoImage(file="img/5H.gif")
CinqV = PhotoImage(file="img/5V.gif")
QuatreH = PhotoImage(file="img/4H.gif")
QuatreV = PhotoImage(file="img/4V.gif")
TroisH = PhotoImage(file="img/3H.gif")
TroisV = PhotoImage(file="img/3V.gif")
DeuxH = PhotoImage(file="img/2H.gif")
DeuxV = PhotoImage(file="img/2V.gif")
#Save
SaveFond = PhotoImage(file="img/SaveFond.gif")
Save = PhotoImage(file="img/Save.gif")
Import = PhotoImage(file="img/Importer.gif")
#Boutons gm4
BoutonMode = Button(window2, text ='Mode', command = Mode)
BoutonAmi = Button(window2, text ='Joueur contre un ami', command = J2)
BoutonFacile = Button(window2, text ='Facile', command = lambda : IA(1))
BoutonMoyen = Button(window2, text ='Moyen', command = lambda : IA(2))
BoutonDifficile = Button(window2, text ='Difficile', command = lambda : IA(3))
#Importation images
zero = PhotoImage(file="img/EauFond.gif")
un = PhotoImage(file="img/explo.gif")
deux = PhotoImage(file="img/avant.gif")
trois = PhotoImage(file="img/milieu.gif")
quatre = PhotoImage(file="img/arriere.gif")
cinq = PhotoImage(file="img/plouf.gif")
six = PhotoImage(file="img/avant1.gif")
sept = PhotoImage(file="img/milieu1.gif")
huit = PhotoImage(file="img/arriere1.gif")
#images règles
regle1 = PhotoImage(file="img/regle1.gif")
regle2 = PhotoImage(file="img/regle2.gif")
regle3 = PhotoImage(file="img/regle3.gif")
#images gm0
imagemenu = PhotoImage(file="img/gm0w1.gif")
imagemenu2 = PhotoImage(file="img/gm0w2resized.gif")
#image gm4
Instruc = PhotoImage(file="img/Instruc.gif")
#page
#3 page+=1
#4 page-=1
pageR=1
Boutonsuivant = Button(window2, text = 'Suivant', command= lambda : gm5(3))
Boutonprec = Button(window2, text = 'Précedent', command= lambda : gm5(4))
#Retour menu
gm0()

Mafenetre.mainloop()
