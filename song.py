"""Relevant File containing songs to be utilized within the Menu Interface"""






from os import remove
import this
from tkinter import font
from turtle import Screen
import pygame, sys
from pygame.locals import KEYDOWN, K_q
from pygame.locals import *
import time

from chords import AChord, AmChord, DChord
from fundamental import Rect




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






def tune1():
    clock = pygame.time.Clock()
    window = _VARS['surf'] 
    rect = pygame.Rect(0, 80, 40, 40)
    time_interval_A_To_Am = 1000 #4 seconds from showing A -> Am
    next_step_time = 0
    AChord()
    current_time = pygame.time.get_ticks() #get current time from when init has been called
    if current_time > next_step_time: #if the current time >0, i.e. if current time is after program has loaded
        next_step_time += time_interval_A_To_Am #sum of 
        rect.x += 40 #move the length of square to the right 
        if rect.x >= 400: #if square gets to end of screen
            rect.x = 0 #start back at beginning
    #window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()      
    clock.tick(1)    
    return


def tune2():
    songLenS = 10 #Length of song (seconds)
    #clock = pygame.time.Clock()
    #clock.get_time()
    i = 0
    while i < songLenS:
        desiredTime = pygame.time.get_ticks()
        i = i + 1
        pygame.time.wait(1000)
        if i == 5:
            AChord()
        if i == 30:
            DChord()
    return 

