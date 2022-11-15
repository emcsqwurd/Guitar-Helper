"""Relevant File containing code related to all text Icons Within the interface"""







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

_VARS['surf'] = pygame.display.set_mode(SCREENSIZE)

#Colours
_COLOUR = {'BL' : 'BLACK', 'O' : 'ORANGE', 'R' : 'RED', 'BU' : 'BLUE', 'Y' : 'YELLOW'}


clock = pygame.time.Clock()








#----------------------Text Inputs-------------------------



#Build Guitar Helper Logo
def GHelper():
    desriedFont = pygame.font.SysFont('Verdana', 30)
    surfaceText = desriedFont.render('Guitar Helper', False, (0, 0, 0))
    screen = _VARS['surf']
    screen.blit(surfaceText, (50,10))
    return surfaceText



#Build Menu Display
def menu():
    desriedFont = pygame.font.SysFont('Verdana', 30)
    surfaceText = desriedFont.render('MENU', False, (0, 0, 0))
    screen = _VARS['surf']
    screen.blit(surfaceText, (1050, 10))
    return 




#Function to label the Notes of the String of the Guitar
def labelNotes():
    divisionsAcross = _VARS['across']
    divisionsDown = _VARS['down']
    vertical_cellsize = (HEIGHT - (PADTOPBOTTOM)*2)/divisionsDown
    horizontal_cellsize = (WIDTH - (PADLEFTRIGHT*2))/divisionsAcross

    desriedFont = pygame.font.SysFont('Verdana', 30)
    screen = _VARS['surf']
    surfaceTextE = desriedFont.render('E', False, (0, 0, 0))
    screen.blit(surfaceTextE, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + vertical_cellsize/4))
    surfaceTextA = desriedFont.render('B', False, (0,0,0))
    screen.blit(surfaceTextA, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + 5*vertical_cellsize/4))
    surfaceTextD = desriedFont.render('G', False, (0, 0, 0))
    screen.blit(surfaceTextD, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + 9*vertical_cellsize/4))
    surfaceTextG = desriedFont.render('D', False, (0, 0, 0))
    screen.blit(surfaceTextG, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + 13*vertical_cellsize/4))
    surfaceTextB = desriedFont.render('A', False, (0, 0, 0))
    screen.blit(surfaceTextB, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + 17*vertical_cellsize/4) )
    surfaceTextE = desriedFont.render('E', False, (0, 0, 0))
    screen.blit(surfaceTextE, (0 + PADLEFTRIGHT + horizontal_cellsize/3, 0 + PADTOPBOTTOM + 21*vertical_cellsize/4))
    return 
    


#Generalised Print Text Function 
#Arguments -> (desired text to be printed, length across on screen, length down on screen)
def printText(TextToPrint, acrossDim, downDim):
    desriedFont = pygame.font.SysFont('Verdana', 30)
    surfaceText = desriedFont.render(TextToPrint, False, (0, 0, 0))
    screen = _VARS['surf']
    screen.blit(surfaceText, (int(acrossDim), int(downDim) ))
    return 



#------------------------------------------------------------------




