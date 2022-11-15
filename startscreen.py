"""Relevant File Related to the start screen animation of the Guitar Helper Interface.
Related code is to be utilized solely for the purpose of the Start Screen Interface."""








import this
from tkinter import font
from turtle import Screen
import pygame, sys
from pygame.locals import KEYDOWN, K_q
from pygame.locals import *
import time
from fundamental import fillBox




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



def filledFirstColumn():
    r1 = fillBox(1,1, _COLOUR['BL'])
    r2 = fillBox(2,1, _COLOUR['BL'])
    r3 = fillBox(3,1, _COLOUR['BL'])
    r4 = fillBox(4,1, _COLOUR['BL'])
    r5 = fillBox(5,1, _COLOUR['BL'])
    r6 = fillBox(6,1, _COLOUR['BL'])
    return r1, r2, r3, r4, r5, r6



