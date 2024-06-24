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
    def __init__(self, screen: pygame.Surface, x, y, width, height, level, picture):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = 5
        self.speed_y = 0
        self.init_velocity = -35
        self.picture = picture
        self.original_image = pygame.image.load(picture)
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.acceleration_y = 2
        self.touching_ground = False
        self.jump_debounce = False
        self.level = level



    def draw(self):
        self.screen.blit(self.image, (self.x, self.y, self.width, self.height))

    def move(self, key_right, key_left, key_up):
        pressed_keys = pygame.key.get_pressed()

        if self.x > 1350:
            self.x = 1350
        if self.x < 0:
            self.x = 0

        if pressed_keys[key_right]:
            self.x += 5
            if self.level.collision_check((self.x, self.y, self.width, self.height)):
                self.x -= 5

        if pressed_keys[key_left]:
            self.x -= 5
            if self.level.collision_check((self.x, self.y, self.width, self.height)):
                self.x += 5

        if pressed_keys[key_up] and self.touching_ground and not self.jump_debounce:
            self.speed_y = self.init_velocity
            self.touching_ground = False
            self.jump_debounce = True
        if not pressed_keys[pygame.K_w]:
            self.jump_debounce = False
    def dophysics(self):
        self.speed_y += self.acceleration_y
        self.y += self.speed_y

        if self.level.collision_check((self.x, self.y, self.width, self.height)):
            self.y -= self.speed_y

            self.speed_y = 0
            self.touching_ground = True
        else:
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

        picture = "unnamed (1).png"
        picture2 = "unnamed (1) (1).png"
        level = Level(screen)
        stick_man1 = Stick_Man(screen, 100, 400, 50, 100, level, picture)
        stick_man2 = Stick_Man(screen, 300, 200, 50, 100, level, picture2)



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


            stick_man1.dophysics()
            stick_man2.dophysics()



            stick_man1.move(pygame.K_d, pygame.K_a, pygame.K_w)
            stick_man1.draw()
            stick_man2.move(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP)
            stick_man2.draw()



                # don't forget the update, otherwise nothing will show up!
            pygame.display.update()

            clock.tick(60)


if __name__ == "__main__":
    main()
