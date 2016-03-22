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
def mode():
    global mode
    if mode=="h":
        mode="v"
    else:
        mode="h"
#Joueur vs Joueur
def J2():
    global joueur
    joueur=2
    global bateau
    bateau=1
    BoutonAmi.destroy()
    BoutonOrdi.destroy()
    gm4()

#Pointeur in game J1
def pointeurJeuJ1(event):
    global bateaux2
    global joueur
    global bateau
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    print(casex)
    print(casey)
    if casex>1 and casey>1 and bateaux2[casey-2,casex-2]!=1 and bateaux2[casey-2,casex-2]!=5:
        window1.unbind('<Button-1>')
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
    global joueur
    global bateau
    casex=ceil(float(0.02)*float(str(event.x)))
    casey=ceil(float(0.02)*float(str(event.y)))
    print(casex)
    print(casey)
    if casex>1 and casey>1 and bateaux1[casey-2,casex-2]!=1 and bateaux1[casey-2,casex-2]!=5:
        window1.unbind('<Button-1>')
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
                        BoutonAmi.place(relx = 0.6, rely =0.1, anchor = E)
                        BoutonOrdi.place(relx = 0.6, rely =0.3, anchor = E)
                        bateau=0
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
            elif bateau==2:
                if casey<8:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0 and bateaux1[casey+1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=7
                        bateaux1[casey+1,casex-2]=8
                        bateau=3
            elif bateau==3:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=8
                        bateau=4
            elif bateau==4:
                if casey<9:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0 and bateaux1[casey,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=7
                        bateaux1[casey,casex-2]=8
                        bateau=5
            elif bateau==5:
                if casey<10:
                    if bateaux1[casey-2,casex-2]==0 and bateaux1[casey-1,casex-2]==0:
                        bateaux1[casey-2,casex-2]=6
                        bateaux1[casey-1,casex-2]=8
                        BoutonAmi.place(relx = 0.6, rely =0.1, anchor = E)
                        BoutonOrdi.place(relx = 0.6, rely =0.3, anchor = E)
                        bateau=0
        print(bateaux1)
        gm4()

#Detection souris J2
def pointeurJ2(event):
    global bateaux2
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
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0 and bateaux2[casey-2,casex+2]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=3
                        bateaux2[casey-2,casex+1]=3
                        bateaux2[casey-2,casex+2]=4
                        bateau=2
            elif bateau==2:
                if casex<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0 and bateaux2[casey-2,casex+1]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=3
                        bateaux2[casey-2,casex+1]=4
                        bateau=3
            elif bateau==3:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=4
                        bateau=4
            elif bateau==4:
                if casex<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0 and bateaux2[casey-2,casex]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=3
                        bateaux2[casey-2,casex]=4
                        bateau=5
            elif bateau==5:
                if casex<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-2,casex-1]==0:
                        bateaux2[casey-2,casex-2]=2
                        bateaux2[casey-2,casex-1]=4
                        bateau=0
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
            elif bateau==2:
                if casey<8:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0 and bateaux2[casey+1,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=7
                        bateaux2[casey+1,casex-2]=8
                        bateau=3
            elif bateau==3:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=8
                        bateau=4
            elif bateau==4:
                if casey<9:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0 and bateaux2[casey,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=7
                        bateaux2[casey,casex-2]=8
                        bateau=5
            elif bateau==5:
                if casey<10:
                    if bateaux2[casey-2,casex-2]==0 and bateaux2[casey-1,casex-2]==0:
                        bateaux2[casey-2,casex-2]=6
                        bateaux2[casey-1,casex-2]=8
                        bateau=0
        print(bateaux2)
        if bateau==0:
            BoutonMode.destroy()
            window1.create_image(0, 0, image = TourJ1, anchor = NW)
            window1.unbind('<Button-1>')
            window2.after(1, wait, 5, time_is_up1)
        else:
            gm4()

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
#Changer gamemode -> 0
def gm0():
    window1.delete(ALL)
    window2.delete(ALL)
    #MENU
    window1.create_image(0, 0, image = imagemenu, anchor = NW)
    window2.create_image(0, 0, image = imagemenu2, anchor = NW)
    BoutonJouer.place(relx = 0.8, rely =0.2, anchor = E)
    BoutonImporter.place(relx = 0.8, rely =0.27, anchor = E)
    BoutonRegles.place(relx = 0.8, rely =0.34, anchor = E)
    BoutonApropos.place(relx = 0.8, rely =0.41, anchor = E)
    BoutonQuitter.place(relx = 0.8, rely =0.48, anchor = E)
#============================================================================
#Changer gamemode -> 1
def gm1():
    BoutonAmi.destroy()
    BoutonOrdi.destroy()
    BoutonMode.destroy()
    BoutonJouer.destroy()
    BoutonImporter.destroy()
    BoutonRegles.destroy()
    BoutonApropos.destroy()
    BoutonQuitter.destroy()
    window1.delete(ALL)
    window2.delete(ALL)
    global joueur
    global bateaux1

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
                elif bateaux1[y,x]==3:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=trois)
                elif bateaux1[y,x]==4:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                elif bateaux1[y,x]==5:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=cinq)
                elif bateaux1[y,x]==6:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=six)
                elif bateaux1[y,x]==7:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=sept)
                elif bateaux1[y,x]==8:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=huit)
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
                elif bateaux2[y,x]==3:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=trois)
                elif bateaux2[y,x]==4:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=quatre)
                elif bateaux2[y,x]==5:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=cinq)
                elif bateaux2[y,x]==6:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=six)
                elif bateaux2[y,x]==7:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=sept)
                elif bateaux2[y,x]==8:
                    window2.create_image(xvoul,yvoul, anchor=NW, image=huit)
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

    lignes1()
    lignes2()

#Detection clic souris
    if joueur==1:
        window1.bind("<Button-1>", pointeurJeuJ1)
    elif joueur==2:
        window1.bind("<Button-1>", pointeurJeuJ2)
#============================================================================
#Changer gamemode -> 2
def gm2():
    BoutonAmi.destroy()
    BoutonOrdi.destroy()
    BoutonMode.destroy()
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
    BoutonAmi.destroy()
    BoutonOrdi.destroy()
    BoutonMode.destroy()
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
    elif joueur==2:
        window1.bind("<Button-1>", pointeurJ2)

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
#Wait
Touche = PhotoImage(file="texte1.gif")
Eau = PhotoImage(file="texte2.gif")
TourJ1 = PhotoImage(file="J1.gif")
TourJ2 = PhotoImage(file="J2.gif")
Restant5 = PhotoImage(file="5.gif")
Restant4 = PhotoImage(file="4.gif")
Restant3 = PhotoImage(file="3.gif")
Restant2 = PhotoImage(file="2.gif")
Restant1 = PhotoImage(file="1.gif")
#Boutons gm4
BoutonMode = Button(window2, text ='Mode', command = mode)
BoutonAmi = Button(window2, text ='Joueur contre un ami', command = J2)
BoutonOrdi = Button(window2, text ='Jouer contre l\'ordinateur', command = Mafenetre.destroy)
#Importation images
zero = PhotoImage(file="EauFond.gif")
un = PhotoImage(file="explo.gif")
deux = PhotoImage(file="avant.gif")
trois = PhotoImage(file="milieu.gif")
quatre = PhotoImage(file="arriere.gif")
cinq = PhotoImage(file="plouf.gif")
six = PhotoImage(file="avant1.gif")
sept = PhotoImage(file="milieu1.gif")
huit = PhotoImage(file="arriere1.gif")
#mode de display
mode="h"
#images gm0
imagemenu = PhotoImage(file="gm0w1.gif")
imagemenu2 = PhotoImage(file="gm0w2resized.gif")
gm0()

Mafenetre.mainloop()
