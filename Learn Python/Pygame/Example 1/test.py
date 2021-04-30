# -*- coding: utf-8 -*-
"""
summary

description

:REQUIRES: pygame package
:TODO: Learn Pygame - Basic Movement and Key Presses
:AUTHOR: Arfaoui Mehdi
:CONTACT: arfaouimehdi20@yahoo.fr
:SINCE: Fri Apr 30 15:55:22 2021
:VERSION: 0.1
"""
#===============================================================================
# PROGRAM METADATA
#===============================================================================
__author__ = 'Arfaoui Mehdi'
__contact__ = 'arfaouimehdi20@yahoo.fr'
__date__ = 'Fri Apr 30 15:55:22 2021'
__version__ = '0.1'

#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
import pygame

#===============================================================================
# METHODS
#===============================================================================


# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()

screen_width, screen_height = 500, 500

# create the display surface object 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Moving object")

# Display object info 

x, y = 100, 100

object_width, object_height = 20, 20

# velocity
object_vel = 5

#RBG colors 
black = (0,0,0)
red = (255,0,0)

FPS = 60

clock = pygame.time.Clock()

run = True
# infinite loop 
while run :

    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get():

        if event.type ==pygame.QUIT :

            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 :

        x -= object_vel

    if keys[pygame.K_RIGHT] and x < (screen_width - object_width):

        x += object_vel

    if keys[pygame.K_UP ] and  y> 0 :

        y -= object_vel

    if keys[pygame.K_DOWN] and y < (screen_height - object_height):

        y += object_vel


    # fill the surface object  
    # with black colour  
    screen.fill(black)           
    # drawing object on screen which is rectangle here 
    pygame.draw.rect( screen, red, (x, y, object_width, object_height))      
    # it refreshes the window
    pygame.display.update()

    clock.tick(FPS)

# closes the pygame window 
pygame.quit()


#===============================================================================
# QUICK REFERENCE
#===============================================================================

 # https://www.pygame.org/news