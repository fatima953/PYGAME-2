import pygame

import random

pygame.init()

sw,sh = 400,400

screen = pygame.display.set_mode((sw,sh))

pygame.display.set_caption('Welcome to coler changing game')

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  
color = random_color()

sr = pygame.Rect(200,200,30,30)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if sr.collidepoint(event.pos):

                color = random_color()

    screen.fill((255,255,255))

    pygame.draw.rect(screen,color,sr)

    pygame.display.flip()

pygame.quit()
