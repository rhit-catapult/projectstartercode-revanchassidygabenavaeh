import pygame
import sys
import main_module
import time
import math


def main():
    # turn on pygame
    pygame.init()
    screen_width = 1434
    screen_height = 805
    screen = pygame.display.set_mode((screen_width, screen_height))
    corndog = pygame.image.load("corndog.jpg")

    font1 = pygame.font.SysFont("elephant", 100)
    caption1 = font1.render("TAGGGY", True, pygame.Color("green"))
    # create a screen
    # TODO: Change the size of the screen as you see fit!


    pygame.display.set_caption("TAG")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(corndog, (screen.get_width() / 2 - corndog.get_width() / 2, 100))
        screen.blit(caption1, (screen.get_width() /2 - caption1.get_width() /2 , screen.get_height() / 2))
        #print(pygame.font.get_fonts())

        pygame.display.update()



if __name__ == "__main__":
    main()