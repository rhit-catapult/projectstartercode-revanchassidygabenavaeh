import pygame
import sys
import random

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

class Scoreboard:
    def __init__(self, screen: pygame.Surface, x, color):
        self.screen = screen
        self.x = x
        self.y = 10
        self.score = 0
        self.color = color
        self.font = pygame.font.SysFont("candara",20, True)

    def draw(self):
        caption = self.font.render(f"It timer: {self.score}", True, self.color)
        self.screen.blit(caption,(self.x , self.y))

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    # TODO: Change the size of the screen as you see fit!
    screen_width = 1434
    screen_height = 805
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cool Project")
    #print(pygame.font.get_fonts())
    redscore = Scoreboard(screen, 10, pygame.Color("red"))
    bluescore = Scoreboard(screen,1000, pygame.Color("blue"))
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((200, 200, 200))
        redscore.draw()
        bluescore.draw()
        redscore.score+=1


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()




if __name__ == "__main__":
    main()
