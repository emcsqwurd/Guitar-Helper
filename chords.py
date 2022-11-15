"""Relevant file containing hard coded Chords from which can be utilized for
implementing songs"""

import this
from tkinter import font
from turtle import Screen
import pygame, sys
from pygame.locals import KEYDOWN, K_q
from pygame.locals import *
import time
from fundamental import fillBox
from text import printText




# CONSTANTS:

SCREENSIZE = WIDTH, HEIGHT = 1200, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 60, 60


# GLOBAL VARS, Using a Dictionary.
_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (20, 20), 'gridCells': 4, 'lineWidth': 2, 'across' : 25, 'down' : 6}

_VARS['surf'] = pygame.display.set_mode(SCREENSIZE) #Added to Constants to ensure correct workings of drawNeck() Function i.e. pygame.draw.line first argument must be surface not boolean

#Colours
_COLOUR = {'BL' : 'BLACK', 'O' : 'ORANGE', 'R' : 'RED', 'BU' : 'BLUE', 'Y' : 'YELLOW'}


clock = pygame.time.Clock()









#-----------------------------CHORDS-------------------------------



#---A---

def AChord():
    AList = []
    b1 = fillBox(2,2, _COLOUR['Y'])
    AList.append(b1)
    b2 = fillBox(2,3, _COLOUR['Y'])
    AList.append(b2)
    b3 = fillBox(4,2, _COLOUR['Y'])
    AList.append(b3)
    #printText('A', 600, 10)
    return AList

def AmChord():
    AmList = []
    b1 = fillBox(2,1, _COLOUR['O'])
    AmList.append(b1)
    b2 = fillBox(3,2, _COLOUR['O'])
    AmList.append(b2)
    b3 = fillBox(4,2, _COLOUR['O'])
    AmList.append(b3)
    #printText('Am', 600, 10)
    return AmList

#---D---

def DChord():
    fillBox(1,2, _COLOUR['BL'])
    fillBox(3,2, _COLOUR['BL'])
    fillBox(2,3, _COLOUR['BL'])
    printText('D', 600, 10)
    return 

def DmChord():
    fillBox(1,1, _COLOUR['R'])
    fillBox(3,2, _COLOUR['R'])
    fillBox(2,3 ,_COLOUR['R'])
    printText('Dm', 600, 10)
    return 

#---G---




 
#FIX POSITIONS
def GChord():
    fillBox(5,2, _COLOUR['O'])
    fillBox(1,3, _COLOUR['O'])
    fillBox(6,3, _COLOUR['O'])
    printText('G', 600, 10)
    return 

def GmChord():
    fillBox(1,1,_COLOUR['R'])
    fillBox(2,1,_COLOUR['R'])
    fillBox(3,1,_COLOUR['R'])
    fillBox(6,1,_COLOUR['R'])
    fillBox(4,3,_COLOUR['R'])
    fillBox(5,3,_COLOUR['R'])
    printText('Gm', 600, 10)
    return 

#---B---

def BChord():
    fillBox(5,2, _COLOUR['R'])
    fillBox(2,4, _COLOUR['R'])
    fillBox(3,4 ,_COLOUR['R'])
    fillBox(4,4, _COLOUR['R'])
    printText('B', 600, 10)
    return 

def BmChord():
    fillBox(1,2, _COLOUR['R'])
    fillBox(5,2 ,_COLOUR['R'])
    fillBox(2,3, _COLOUR['R'])
    fillBox(3,4, _COLOUR['R'])
    fillBox(4,4, _COLOUR['R'])
    printText('Bm', 600, 10)
    return     


#---E---

def EChord():
    fillBox(3,1, _COLOUR['BU'])
    fillBox(4,2, _COLOUR['BU'])
    fillBox(5,2, _COLOUR['BU'])
    printText('E', 600, 10)
    return     

def EmChord():
    fillBox(4,2, _COLOUR['R'])
    fillBox(5,2, _COLOUR['R'])
    printText('Em', 600, 10)
    return     


#---C---

def CChord():
    fillBox(2,1, _COLOUR['BL'])
    fillBox(4,2, _COLOUR['BL'])
    fillBox(5,3, _COLOUR['BL'])
    printText('C', 600, 10)
    return 

def CmChord():
    fillBox(1,1, _COLOUR['R'])
    fillBox(5,1, _COLOUR['R'])
    fillBox(2,2, _COLOUR['R'])
    fillBox(3,3, _COLOUR['R'])
    fillBox(4,3, _COLOUR['R'])
    printText('Cm', 600, 10)
    return 


#-------------------------------END Chords-----------------------




