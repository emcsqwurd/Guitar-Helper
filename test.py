"""Relevant File containing example code found online to help with the implementation
of certain Features for the Guitar Helper Interface"""


from pickle import FALSE
import numpy as np
import pygame
import time
import sys
import time
import random



def test():
    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([320,240])
    sys_font = pygame.font.SysFont(pygame.font.get_default_font(), 18)

    pygame.display.set_caption("Quiz")
    nums_left = 0  # initialise the  counters
    nums_right = 0  
    done = False

    questions = ["Who?", "What?", "Where?", "When?", "Why?"]

    # states: 0: init, 10: select a question, 20: wait for answer, 30: Answered
    state = 0
    while not done:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if state == 0:
                    state = 10
            elif event.type == pygame.MOUSEBUTTONUP:
                if state == 20:
                    if event.button == 1:  # left
                        nums_left += 1
                        state = 30
                    elif event.button == 2: # middle
                        pass
                    elif event.button == 3: # right
                        nums_right += 1
                        state = 30
                elif state == 30:
                    state = 10 # ask a new question

        # Clear Background
        screen.fill(pygame.color.Color("white"))
        #  Manage state
        if state == 0:
            question_txt = sys_font.render("Press any key to start!", True, pygame.color.Color("violet"))
        elif state == 10:
            # choose a random question
            question = random.choice(questions)
            question_txt = sys_font.render(question, True, pygame.color.Color("seagreen"))
            # comment out the line below to replicate buggy behaviour
            state = 20  
        elif state == 20:
            # we're just waiting here, perhaps indicate the mouse should be clicked
            pass
        elif state == 30:
            question_txt = sys_font.render("Click for a new question", True, pygame.color.Color("turquoise"))
        else:
            raise NotImplementedError  # shouldn't get here

        # always draw the score
        score_txt = sys_font.render(f"Left: {nums_left} Right: {nums_right}", True, pygame.color.Color("olivedrab"))
        # update the screen
        screen.blit(question_txt, (20, 20))
        screen.blit(score_txt, (20, 220))
        # Frame Change
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    return 
#print(test())



def test2():
    pygame.init()
    window = pygame.display.set_mode((400, 200)) #dimensions of display window 
    clock = pygame.time.Clock() #initiate pygame clock
    rect = pygame.Rect(0, 80, 40, 40) #dimensions of red rectangle 

    time_interval = 1000 #time taken for red square to move each incrament to the right (in milliseconds), i.e. time between successive movements
    next_step_time = 0

    run = True
    while run: #when the pygame window is running 
        for event in pygame.event.get(): #for each event during the events within the pygame program
            if event.type == pygame.QUIT: #if the event type is to quit the game 
                run = False #then stop running the game

        current_time = pygame.time.get_ticks() #get current time from when init has been called
        if current_time > next_step_time: #if the current time >0, i.e. if current time is after program has loaded
            next_step_time += time_interval #sum of 
        
            rect.x += 40 #move the length of square to the right 
            if rect.x >= 400: #if square gets to end of screen
                rect.x = 0 #start back at beginning

        window.fill(5)
        pygame.draw.rect(window, (255, 0, 0), rect)
        pygame.display.flip()
        clock.tick(1) #?????? <1 values breaks program
    pygame.quit()
    return 
print(test2())





