import pygame

# intialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


