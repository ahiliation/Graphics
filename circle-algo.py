import os
import pygame
import time
import random
import math
import numpy

from math import pi

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


size = [800, 600]
screen = pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
#x = 0.0
#y = 0.0
#z = 0.0
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
#    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    
    for x in numpy.arange(0,1000,1):
#        x = x + 0.1
        for y in numpy.arange(0,1000, 0.25):
#            y = y + 0.1
#    x = random.randint(0,683)
#    y = random.randint(0,384)
#   i = i + 0.1
#   j = j + 0.1
#            x = 683 + x
#            y = 384 + y
            a = x*x
            b = y*y
    
            if ( math.sqrt(a + b) == 100 ):
       
                pygame.draw.line(screen, GREEN, [383.0 + x, 184.0 - y], [383.0 + x, 184.0 - y], 2)
                pygame.draw.line(screen, GREEN, [383.0 + x, 184.0 + y], [383.0 + x, 184.0 + y], 2)
                pygame.draw.line(screen, GREEN, [383.0 - x, 184.0 + y], [383.0 - x, 184.0 + y], 2)
                pygame.draw.line(screen, GREEN, [383.0 - x, 184.0 - y], [383.0 - x, 184.0 - y], 2)
                print x , y
                time.sleep(0.1)
                pygame.display.flip()

pygame.quit()
