import pygame
import sys

WHITE= (225, 225,225)
BLACK=(0,0,0)
class Level:
    def __init__(self,screen: pygame.Surface):
        self.screen = screen
        self.platform_pos = []
        self.platform_pos.append((100, 505, 300, 20))
        self.platform_pos.append((550, 250, 300, 20))
        self.platform_pos.append((800, 600, 300, 20))
        self.platform_pos.append((1300, 450, 300, 20))
        self.platform_pos.append((0, 775, 1500, 30))
    def draw(self):
        for platform in self.platform_pos:
            pygame.draw.rect(self.screen, BLACK, platform)
    def collision_check(self, rect):
        rect=pygame.Rect(rect)
        for platform in self.platform_pos:
            if rect.colliderect(platform):
                return True
        return False






class Stick_Man:
    def __init__(self, screen: pygame.Surface, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = 5
        self.speed_y = 0
        self.init_velocity = -35
        self.original_image = pygame.image.load("Standing(Middle).png")
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.acceleration_y = 2
        self.touching_ground = False


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y, self.width, self.height))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.x > 1350:
            self.x = 1350
        if self.x < 0:
            self.x = 0
        if pressed_keys[pygame.K_RIGHT]:
            self.x += 5
        if pressed_keys[pygame.K_LEFT]:
            self.x -= 5
        if pressed_keys[pygame.K_UP] and self.touching_ground:
            self.speed_y = self.init_velocity
            self.touching_ground = False

def main():
      # turn on pygame
        pygame.init()

        # create a screen
        # TODO: Change the size of the screen as you see fit!
        screen_width = 1434
        screen_height = 805
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Cool Project")


        stick_man2 = Stick_Man(screen, 400, 605, 100, 100)
        level=Level(screen)



        frame_counter1 = 0
        frame_counter2 = 0
        # let's set the framerate
        clock = pygame.time.Clock()
        running= True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            screen.fill((200,200,200))



            level.draw()


            stick_man2.speed_y += stick_man2.acceleration_y
            stick_man2.y += stick_man2.speed_y

            if level.collision_check((stick_man2.x, stick_man2.y,stick_man2.width, stick_man2.height)):
                stick_man2.y -= stick_man2.speed_y
                stick_man2.speed_y=0
                stick_man2.touching_ground = True



            stick_man2.move()
            stick_man2.draw()

                # don't forget the update, otherwise nothing will show up!
            pygame.display.update()

            clock.tick(60)


if __name__ == "__main__":
    main()
