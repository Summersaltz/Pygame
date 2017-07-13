#Pygame
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

#define colours (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame and create our window
pygame.init()
pygame.mixer.init() #enalbles sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update
    #draw/render
    screen.fill(BLACK)
    #after drawing everyting, flip the display
    pygame.display.flip()
pygame.quit()
    

