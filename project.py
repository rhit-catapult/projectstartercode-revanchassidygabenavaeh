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
    corndog = pygame.image.load("../pygamestartercode-rhit-naveR/00-IntroToPython/replit_play_example/corndog.jpg")
    red_person = pygame.image.load("hit(red) (1).png")
    blue_person = pygame.image.load("hit(blue).png")
    tag_thing = pygame.image.load("Tag-6-25-2024.png")

    font1 = pygame.font.SysFont("elephant", 100)
    # caption1 = font1.render("TAGGGY", True, pygame.Color("green"))
    # create a screen
    # TODO: Change the size of the screen as you see fit!

    drop_thing1 = Drop_Things(screen, -600, 60)
    drop_thing2 = Drop_Things(screen, -600, 1374)
    play_button = button_start.TextButton(screen, screen.get_width() / 2, 525, "             play             ")
    clock = pygame.time.Clock()
    pygame.display.set_caption("TAG")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.is_clicked_by(event.pos):

                    #print("You clicked the play button.")
                    main_module.main_game_loop(screen)
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

        screen.blit(tag_thing, (screen.get_width() / 2 - tag_thing.get_width() / 2 + 75, -35))
        screen.blit(red_person, (140, 402))
        screen.blit(blue_person, (1000, 402))
        # screen.blit(caption1, (screen.get_width() /2 - caption1.get_width() /2 , screen.get_height() / 2))
        # print(pygame.font.get_fonts())
        play_button.draw()

        pygame.display.update()



if __name__ == "__main__":
    main()