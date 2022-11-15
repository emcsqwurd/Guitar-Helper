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





# CONSTANTS:

SCREENSIZE = WIDTH, HEIGHT = 1200, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 60, 60


# GLOBAL VARS, Using a Dictionary.
_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (20, 20), 'gridCells': 4, 'lineWidth': 2, 'across' : 25, 'down' : 6}



#Colours
_COLOUR = {'BL' : 'BLACK', 'O' : 'ORANGE', 'R' : 'RED', 'BU' : 'BLUE', 'Y' : 'YELLOW'}


clock = pygame.time.Clock()



#--------------------MAIN Script to be ran-----------------




def main():

    pygame.init()  # Initial Setup

    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)

    # The loop proper, things inside this loop will
    # be called over and over until you exit the window

    running = True
    while running:

        #Check all events
        checkEvents()


        _VARS['surf'].fill(GREY)

        #Displaying Neck of Guitar with Strings included
        drawString(25, 6)

        #Start Screen Animation
        #filledColumn()

        #Input Desired Chords
        #DChord()
        #GChord()
        #AmChord()

        #Text
        GHelper()
        menu()
        labelNotes()
        

        #tune
        #tune1()
       

        pygame.display.update()


    #Clicking Functions
    #clickMenu()    

    return 
        





#---------------------------END Main Script to be run---------------










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


#----------------------END Events under consideration-----------









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
def drawNeck(divisionsAcross, divisionsDown):

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





#Function to draw the strings onto the Neck of the Guitar
def drawString(divisionsAcross, divisionsDown):

    #Firstly obtain Neck Grid of Guitar
    drawNeck(_VARS['across'], _VARS['down'])

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











#-----------------------------CHORDS-------------------------------



#---A---

def AChord():
    b1 = fillBox(2,2, _COLOUR['Y'])
    b2 = fillBox(2,3, _COLOUR['Y'])
    b3 = fillBox(4,2, _COLOUR['Y'])
    printText('A', 600, 10)
    return b1, b2, b3

def AmChord():
    b1 = fillBox(2,1, _COLOUR['O'])
    b2 = fillBox(3,2, _COLOUR['O'])
    b3 = fillBox(4,2, _COLOUR['O'])
    printText('Am', 600, 10)
    return b1, b2, b3

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






#-------------------------------START Song-------------------------





def tune1():
    time_interval_A_To_Am = 4000 #4 seconds from showing A -> Am
    return



#-----------------------END Song----------------------------------------















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





#----------------------------Starting Screen Animation-------------


def filledColumn():
    r1 = fillBox(1,1, _COLOUR['BL'])
    r2 = fillBox(2,1, _COLOUR['BL'])
    r3 = fillBox(3,1, _COLOUR['BL'])
    r4 = fillBox(4,1, _COLOUR['BL'])
    r5 = fillBox(5,1, _COLOUR['BL'])
    r6 = fillBox(6,1, _COLOUR['BL'])
    return r1, r2, r3, r4, r5, r6











#---------------------- On-Click Functions-------------------------


def menuToClick():
    return 

















"""
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
        
        elif event.type == MOUSEBUTTONDOWN:
            clickedMenu = menu() #what you want to click e.g. menu
            if clickedMenu(event.pos):
                running = False  

        elif event.type == MOUSEBUTTONDOWN:
            clickedFilled = 0
            if clickedFilled(event.pos):
                return 
                

    return 

"""



#Run File
if __name__ == '__main__':
    main()








