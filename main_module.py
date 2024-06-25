import pygame
import sys
import random
import scoreboard_module
import countdown_module
# 27

WHITE= (225, 225,225)
BLACK=(0,0,0)
class Level:
    def __init__(self,screen: pygame.Surface):
        self.screen = screen
        self.platform_pos = []
        self.platform_pos.append((100, 505, 300, 20))
        self.platform_pos.append((550, 250, 300, 20))
        self.platform_pos.append((800, 600, 300, 20))
        self.platform_pos.append((1100, 400, 250, 20))
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
    def change_sprite(self, sprite_number, direction):
        if sprite_number ==0:
            self.image = self.original_image
        elif sprite_number ==1:
            self.image= self.sticky_man2
            if direction ==1:
                self.image=pygame.transform.flip(self.image, True, False)


        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=self.rect.center)



    def __init__(self, screen: pygame.Surface, x, y, width, height, level, picture, sticky_man2, is_it=False):
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
        self.image2 = pygame.image.load("corndog.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.acceleration_y = 2
        self.touching_ground = False
        self.jump_debounce = False
        self.level = level
        self.is_it = is_it
        self.normal_speed = 10
        self.it_speed = 15
        self.sticky_man2 = pygame.image.load(sticky_man2)
        self.sticky_man2 = pygame.transform.scale(self.sticky_man2, (self.width, self.height))
        self.direction=1

    def is_touching(self,other_stickman):
        my_rect = pygame.Rect(self.x, self.y, self.width,self.height)
        other_rect=pygame.Rect(other_stickman.x, other_stickman.y, other_stickman.width,other_stickman.height)
        return my_rect.colliderect(other_rect)



    def draw(self):
        if self.is_it:
            self.screen.blit(self.image2, (self.x,self.y))
        self.screen.blit(self.image, (self.x, self.y, self.width, self.height))

    def move(self, key_right, key_left, key_up, key_tag):
        jump_sound = pygame.mixer.Sound("roblox-gravity-coil-sound-effect-made-with-Voicemod.mp3")
        pressed_keys = pygame.key.get_pressed()

        if self.x > 1350:
            self.x = 0
        if self.x < 0:
            self.x = 1350

        speed = self.normal_speed
        if self.is_it:
            speed = self.it_speed

        if pressed_keys[key_right]:
            self.direction=1
            self.x += speed
            if self.level.collision_check((self.x, self.y, self.width, self.height)):
                self.x -= speed

        if pressed_keys[key_left]:
            self.direction=-1
            self.x -= speed
            if self.level.collision_check((self.x, self.y, self.width, self.height)):
                self.x += speed
        if pressed_keys[key_tag]:
            self.change_sprite(1, self.direction)
        else:
            self.change_sprite(0, self.direction)



        if pressed_keys[key_up] and self.touching_ground and not self.jump_debounce:
            jump_noise = random.randint(1, 10)
            if jump_noise == 3:
                jump_sound.play()
            self.speed_y = self.init_velocity
            self.touching_ground = False
            self.jump_debounce = True
        if not pressed_keys[key_up]:
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
        picture2 = "BLUE IDLE (1).png"
        level = Level(screen)

        is_game_about_to_start = False
        cooldown_counter = 90

        is_player_one_it_next = random.randint(0,1)== 0
        stick_man1 = Stick_Man(screen, 100, 400, 50, 100, level, picture, 'hit(red) (1).png', False)
        stick_man2 = Stick_Man(screen, 300, 200, 50, 100, level, picture2, 'hit(blue).png', False)
        stick_man1.sticky_man2 = pygame.transform.flip(stick_man1.sticky_man2, True, False)

        redscore = scoreboard_module.Scoreboard(screen, 10, pygame.Color("red"))
        bluescore = scoreboard_module.Scoreboard(screen, 1000, pygame.Color("blue"))
        countdownscreen = countdown_module.Countdown(screen)
        pygame.mixer.music.load("easy-arcade-hartzmann-main-version-28392-02-32.mp3")
        pygame.mixer.music.play(-1)
        frame_counter1 = 0
        frame_counter2 = 0
        # let's set the framerate
        clock = pygame.time.Clock()
        running= True

        while running:
            clock.tick(60)
            hit_sound = pygame.mixer.Sound("hard-slap-46388.mp3")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[pygame.K_DOWN]:
                        if stick_man2.is_it:
                            if stick_man2.is_touching(stick_man1):
                                bluescore.stop()
                                stick_man2.is_it = False
                                is_player_one_it_next= True
                                cooldown_counter= 90
                                hit_sound.play()

                    if pressed_keys[pygame.K_s]:
                        if stick_man1.is_it:
                            if stick_man1.is_touching(stick_man2):
                                redscore.stop()
                                stick_man1.is_it = False
                                is_player_one_it_next = False
                                cooldown_counter = 90
                                hit_sound.play()

                    if pressed_keys[pygame.K_h]:
                        redscore.stop()


            screen.fill((200,200,200))
           # print(cooldown_counter)
            if cooldown_counter > 0:
                cooldown_counter -= 1
                if cooldown_counter == 0:
                    countdownscreen.start()
                    is_game_about_to_start = True
            if is_game_about_to_start and not countdownscreen.is_timer_running:
                is_game_about_to_start = False
                if is_player_one_it_next:
                    stick_man1.is_it = True
                    redscore.start()
                else:
                    stick_man2.is_it = True
                    bluescore.start()




            level.draw()


            stick_man1.dophysics()
            stick_man2.dophysics()



            stick_man1.move(pygame.K_d, pygame.K_a, pygame.K_w,pygame.K_s)
            stick_man1.draw()
            stick_man2.move(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)
            stick_man2.draw()
            redscore.draw()
            bluescore.draw()




            countdownscreen.draw()
            pygame.display.update()




if __name__ == "__main__":
    main()
