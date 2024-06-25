import pygame
import sys
import time
import math

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

class Countdown:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("candara",500, True)
        self.is_timer_running = False
        self.start_time = 0

    def draw(self):
        if not self.is_timer_running:
            return
        #pygame.draw.rect(self.screen, pygame.Color(0,0,0,250), (0,0,self.screen.get_width(),self.screen.get_height()))
        s = pygame.Surface((self.screen.get_width(), self.screen.get_height()))  # the size of your rect
        s.set_alpha(200)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        self.screen.blit(s, (0, 0))

        display_time = 3 - (time.time() - self.start_time)
        display_time = math.ceil(display_time)
        caption = self.font.render("{:.0f}".format(display_time), True, (200,200,0))
        self.screen.blit(caption,(self.screen.get_width() / 2 - caption.get_width() / 2 , 150))
        if display_time <= 0:
            self.is_timer_running = False


    def start(self):
        self.is_timer_running = True
        self.start_time = time.time()




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
    #redscore = Scoreboard(screen, 10, pygame.Color("red"))
    #bluescore = Scoreboard(screen,1000, pygame.Color("blue"))
    countdown = Countdown(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[pygame.K_j]:

                    countdown.start()




        screen.fill((200, 200, 200))
        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + 0, 162 + 0), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + 0, 162 + 0), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        pygame.draw.circle(screen, (200, 0, 10), (320, 245), 25, )

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        pygame.draw.rect(screen, (0, 175, 175), (175, 300, 300, 75), )

        pygame.draw.arc(screen, (100, 0, 175), (150, 100, 350, 123), (50), (276))

        countdown.draw()



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()




if __name__ == "__main__":
    main()
