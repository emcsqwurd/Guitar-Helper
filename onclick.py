"""Relevant File containing code related to on click functions of the interface"""





import this
from tkinter import font
from turtle import Screen
import pygame, sys
from pygame.locals import KEYDOWN, K_q
from pygame.locals import *
import time




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










#---------------------- On-Click Functions-------------------------


def menuToClick():
    return 











