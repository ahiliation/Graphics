import os
import pygame
import time
import random
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


#blockSize = 20 #Set the size of the grid block
#for x in range(0, 800, blockSize):
#    for y in range(0, 600, blockSize):
#        rect = pygame.Rect(x, y, blockSize, blockSize)
#        pygame.draw.rect(screen, WHITE, rect, 1)


count = 0

while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop


#    count = 0
    while (count < 21):
       
#    for draw in range(26):
#    while True:
        count = count + 1
        c = random.randint(1,50)
        x = random.randint(1,800)
        y = random.randint(1,600)
#        y1 = m*x + c
#        x1 = (y - c)/m
        x1 = random.randint(1,800)
        y1 = random.randint(1,600)
        m = random.randint(0,1)
        n = 1 - m 
        midx = (x+x1)/2
        midy = (y+y1)/2
        print(x,y)
        print(x1,y1)
        p = m + n
        x2 = (m*x+n*x1)/p
        y2 = (m*y+n*y1)/p
        # if y < 600:
#        print ("hello")
        print (count)
#        if draw > 20:
#            break
        pygame.draw.line(screen, BLUE, [x1, y1], [x,y], 1)
        time.sleep(0.1)
        pygame.draw.circle(screen, GREEN, (x2,y2), 20) # Here <<<
      #  m = (y1 - y)/(x1 - x)
        pygame.display.flip()
       

pygame.quit()

