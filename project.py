import pygame
import sys
import random
import time



def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1434, 805))

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((17, 20, 132))
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (200, 605, 300, 20))
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (400, 900, 300, 20))
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
