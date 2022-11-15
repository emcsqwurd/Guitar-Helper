"""File to Run the Main Script implementing Program, along with all relevant 
Executable Events.  This file also contains all relevant constants required for
the Program"""

from __future__ import division
from contextlib import redirect_stderr
import sys
import this
from tkinter import font
from turtle import Screen
import pygame, sys
from pygame.locals import KEYDOWN, K_q
from pygame.locals import *
import time
from fundamental import drawString
from text import GHelper, menu, labelNotes
from song import tune1, tune2
from startscreen import filledFirstColumn





# CONSTANTS-------------------------------------------------------------------------------


"""Screen Dimensions"""
SCREENSIZE = WIDTH, HEIGHT = 1200, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 60, 60


"""Screen and Neck Constants"""
_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (20, 20), 'gridCells': 4, 'lineWidth': 2, 'across' : 25, 'down' : 6} #GLOBAL VARS, Using a Dictionary.


"""Colours through means of a Dictionary"""
_COLOUR = {'BL' : 'BLACK', 'O' : 'ORANGE', 'R' : 'RED', 'BU' : 'BLUE', 'Y' : 'YELLOW'}


clock = pygame.time.Clock()


#END CONSTANTS--------------------------------------------------------------------------------------









#--------------------Checking Events Functions------------------


#Function to check the Events of the game window
def checkEvents():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


        #click to Quit - may require additional code to ensure only exit when icon is clicked
        """
        elif event.type == MOUSEBUTTONDOWN:
            clickedMenu = menu() #what you want to click e.g. menu
            if clickedMenu(event.pos):
                running = False  

        elif event.type == MOUSEBUTTONDOWN:
            clickedFilled = 0
            if clickedFilled(event.pos):
                return 
                """
    return


def main():

    pygame.init()  # Initial Setup

    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE) #setting surface to the screen size dimensions

    # The loop proper, things inside this loop will
    # be called over and over until you exit the window

    running = True
    while running:

        """Check all events"""
        checkEvents()

        _VARS['surf'].fill(GREY)

        """Displaying Neck of Guitar with Strings included"""
        drawString()

        """Start Screen Animation"""
        #filledFirstColumn()

        """Input Desired Chords"""
        #DChord()
        #GChord()
        #AmChord()

        """Text Displays"""
        GHelper()
        menu()
        labelNotes()
        
        """Song Inputs"""
        #tune2()
       
        pygame.display.update()

    """Clicking Functions"""
    #clickMenu()    
    return 
        

#Run File
if __name__ == '__main__':
    main()

