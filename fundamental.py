"""Relevant File containing all relevant Fundamental Functions (Building Blocks) for 
Program.  Such Functions may not be Explicitly implemented, however contain insight 
into the 'make-up' describing how the Program has been Designed"""


from __future__ import division
from contextlib import redirect_stderr
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













#-------------------START Fundamental Functions------------------------------------------






#Sample of drawing rectangle to re-iterate system (method) of producing diagrams
def drawRectangle():
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)

    # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)






#Function to obtain grid for the Neck of Guitar
def drawNeck():

    divisionsAcross = _VARS['across']
    divisionsDown = _VARS['down']
    # DRAW Rectangle
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)

    # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # Get cell size
    horizontal_cellsize = (WIDTH - (PADLEFTRIGHT*2))/divisionsAcross
    vertical_cellsize = (HEIGHT - (PADTOPBOTTOM*2))/divisionsDown

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisionsAcross):
            pygame.draw.line(
                _VARS['surf'], BLACK,
                (0 + PADLEFTRIGHT+(horizontal_cellsize*x), 0 + PADTOPBOTTOM),
                (0 + PADLEFTRIGHT+horizontal_cellsize*x, HEIGHT - PADTOPBOTTOM), 4)
    
    # HORITZONTAL DIVISION
    for x in range(divisionsDown):
            pygame.draw.line(
                _VARS['surf'], BLACK,
                (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)),
                (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)), 2)
    return 





#Function to draw the strings onto the Neck of the Guitar
def drawString():
    divisionsAcross = _VARS['across']
    divisionsDown = _VARS['down']

    #Firstly obtain Neck Grid of Guitar
    drawNeck()

    #Obtaining size of each vertical and horizontal cell for Neck of Guitar
    vertical_cellsize = (HEIGHT - (PADTOPBOTTOM)*2)/divisionsDown
    horizontal_cellsize = (WIDTH - (PADLEFTRIGHT*2))/divisionsAcross

    #Loop to put strings over all cells on Neck of Guitar
    for rowLine in range(divisionsDown):
        #for columnLine in range(divisionsAcross):

        #Fitting Strings to Right Location (midpoint between row lines of grid) on Neck
        rowLine = rowLine + vertical_cellsize/100
        
        #Drawing strings
        pygame.draw.line( _VARS['surf'], 'RED',
                    ( 0 + PADLEFTRIGHT + horizontal_cellsize , 0 + PADTOPBOTTOM +  (vertical_cellsize * rowLine)),
                    ((WIDTH) - PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize * rowLine)), 2)

    return 







# Draw filled rectangle at coordinates
def drawSquareCell(x, y, dimX, dimY, colour):
    pygame.draw.rect(
     _VARS['surf'], colour,
     (x, y, dimX, dimY)
)







#Function to fill a 'cell' on the Neck of the Guitar - Think
#of the Neck of Guitar as grid (Matrix) - Hence fillBox(2,2) 
#Will fill the Cell (2,2) on the Neck of the Guitar - To be utilised
#When representing Chords or Notes (---TWEAK---)
def fillBox(desiredColumn, desiredRow, colour):

    #Getting dimensions
    divisionsAcross = _VARS['across']
    divisionsDown = _VARS['down']

    #Obtaining Grid with cell sizes
    #drawNeck(divisionsAcross, divisionsDown)
    vertical_cellsize = (HEIGHT - (PADTOPBOTTOM)*2)/divisionsDown
    horizontal_cellsize = (WIDTH - (PADLEFTRIGHT*2))/divisionsAcross
    
    drawSquareCell(
        horizontal_cellsize + (horizontal_cellsize*desiredRow)+ (0 + PADLEFTRIGHT) - horizontal_cellsize, 
        (vertical_cellsize*desiredColumn) + (0 + PADTOPBOTTOM) - vertical_cellsize + 1,
        horizontal_cellsize,
        vertical_cellsize, colour)
                
    return 






#-------------------END Fundamental Functions-----------------------------


