import pygame
import sys
import main_module
import time
import math
import button_start
class Drop_Things:
    def __init__(self, screen: pygame.surface, y, x):
        self.screen = screen
        self.speed_y = 5
        self.color = "green"
        self.y = y
        self.x = x


    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + 1, self.y + 500), 50)

    def move(self):
        self.y += self.speed_y

    def Off_Screen(self):
        return self.y > self.screen.get_height()

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

    drop_thing1 = Drop_Things(screen, -600, 60)
    drop_thing2 = Drop_Things(screen, -600, 1374)
    play_button = button_start.TextButton(screen, screen.get_width() / 2, 600, "             play             ")
    clock = pygame.time.Clock()
    pygame.display.set_caption("TAG")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if drop_thing1.Off_Screen():
            drop_thing1.y = -600
            drop_thing2.y = -600
        screen.fill((0, 0, 0))
        drop_thing1.move()
        drop_thing1.draw()
        drop_thing2.move()
        drop_thing2.draw()

        screen.blit(corndog, (screen.get_width() / 2 - corndog.get_width() / 2, 100))
        screen.blit(caption1, (screen.get_width() /2 - caption1.get_width() /2 , screen.get_height() / 2))
        #print(pygame.font.get_fonts())
        play_button.draw()

        pygame.display.update()



if __name__ == "__main__":
    main()