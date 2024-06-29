import pygame
import sys
import random
import scoreboard_module
import countdown_module
import game_over_tag
# 27

WHITE= (225, 225,225)
BLACK=(0,0,0)
# print(pygame.font.get_fonts())
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
            pygame.draw.rect(self.screen, pygame.Color(100, 100, 100), platform)
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
        font1 = pygame.font.SysFont("comicsansms", 28)
        self.caption1 = font1.render("IT", True, pygame.Color(0,120,0))
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
        self.direction=-1
        self.jump_sound = pygame.mixer.Sound("roblox-gravity-coil-sound-effect-made-with-Voicemod.mp3")

    def is_touching(self,other_stickman):
        my_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        other_rect=pygame.Rect(other_stickman.x, other_stickman.y, other_stickman.width,other_stickman.height)
        return my_rect.colliderect(other_rect)



    def draw(self):
        if self.is_it:
            self.screen.blit(self.caption1, (self.x+5,self.y-35))
        self.screen.blit(self.image, (self.x, self.y,200, 200))

    def move(self, key_right, key_left, key_up, key_tag):
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
                self.jump_sound.play()
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
    pygame.init()

    pygame.display.set_caption("TAG")
    screen_width = 1434
    screen_height = 805
    screen = pygame.display.set_mode((screen_width, screen_height))
    main_game_loop(screen)

def get_random_backgrounds(screen):
    a = random.randint(1, 6)
    if a == 1:
        image_thing = pygame.image.load(
            "../pygamestartercode-rhit-naveR/00-IntroToPython/replit_play_example/corndog.jpg")
    if a == 2:
        image_thing = pygame.image.load("day_image.jpg")
    if a == 3:
        image_thing = pygame.image.load("sunset_image.jpg")
    if a == 4:
        image_thing = pygame.image.load("night_image.jpg")
    if a == 5:
        image_thing = pygame.image.load("city scape.jpg")
    if a == 6:
        image_thing = pygame.image.load("mario.jpg")
    return pygame.transform.scale(image_thing, (screen.get_width(), screen.get_height()))

def main_game_loop(screen):

      # turn on pygame


        BLACK=(0,0,0)
        IMAGE_SIZE = 470
        TEXT_HEIGHT = 30
        # create a screen
        # TODO: Change the size of the screen as you see fit




        tag_image = pygame.image.load("Tag-6-25-2024.png")
        tag_image = pygame.transform.scale(tag_image,(tag_image.get_width()*0.5, tag_image.get_height()*0.5))
        font1 = pygame.font.SysFont("elephant", 28)

        caption1 = font1.render("Stickyman: Ultimate Tag", True, pygame.Color(BLACK))


        picture = "unnamed (1).png"
        picture2 = "BLUE IDLE (1).png"
        level = Level(screen)

        is_game_about_to_start = False
        cooldown_counter = 1
        tag_counter = 0

        is_player_one_it_next = random.randint(0,1)== 0
        stick_man1 = Stick_Man(screen, 100, 400, 50, 100, level, picture, 'hit(red) (1).png', False)
        stick_man2 = Stick_Man(screen, 300, 200, 50, 100, level, picture2, 'hit(blue).png', False)
        stick_man1.sticky_man2 = pygame.transform.flip(stick_man1.sticky_man2, True, False)

        redscore = scoreboard_module.Scoreboard(screen, True, pygame.Color("red"))
        bluescore = scoreboard_module.Scoreboard(screen, False, pygame.Color("blue"))
        countdownscreen = countdown_module.Countdown(screen)
        pygame.mixer.music.load("easy-arcade-hartzmann-main-version-28392-02-32.mp3")
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()


        background_image = get_random_backgrounds(screen)

        hit_sound = pygame.mixer.Sound("hard-slap-46388.mp3")
        running= True



        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[pygame.K_RALT]:
                        if stick_man2.is_it:
                            if stick_man2.is_touching(stick_man1):
                                bluescore.stop()
                                stick_man2.is_it = False
                                is_player_one_it_next= True
                                tag_counter=30
                                cooldown_counter= 30
                                hit_sound.play()

                    if pressed_keys[pygame.K_q]:
                        if stick_man1.is_it:
                            if stick_man1.is_touching(stick_man2):
                                redscore.stop()
                                stick_man1.is_it = False
                                is_player_one_it_next = False
                                tag_counter=30
                                cooldown_counter = 30
                                hit_sound.play()

            screen.blit(background_image, (0, 0))
            pygame.draw.rect(screen, pygame.Color("grey"), (0, 0, 1450, 50))
            screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2, 5))
            lose_time = 45

            if redscore.get_display_time() > lose_time:
                game_over_tag.run_game_over_loop(screen, False)
            if bluescore.get_display_time() > lose_time:
                game_over_tag.run_game_over_loop(screen, True)
            if bluescore.get_display_time() > lose_time or redscore.get_display_time() > lose_time:
                is_game_about_to_start = False
                cooldown_counter = 1
                tag_counter = 0
                redscore.score = 0
                bluescore.score = 0
                redscore.is_timer_running = False
                bluescore.is_timer_running = False
                stick_man1.is_it = False
                stick_man2.is_it = False



           # print(cooldown_counter)
            if cooldown_counter > 0:
                cooldown_counter -= 1
                if cooldown_counter == 0:
                    countdownscreen.start()
                    is_game_about_to_start = True
            if is_game_about_to_start and not countdownscreen.is_timer_running:
                is_game_about_to_start = False
                background_image = get_random_backgrounds(screen)
                if is_player_one_it_next:
                    stick_man1.is_it = True
                    redscore.start()

                else:
                    stick_man2.is_it = True
                    bluescore.start()




            level.draw()
            pygame.draw.rect(screen, pygame.Color("black"), (100, 505, 300, 20), 4)
            pygame.draw.rect(screen, pygame.Color("black"), (550, 250, 300, 20), 4)
            pygame.draw.rect(screen, pygame.Color("black"), (800, 600, 300, 20), 4)
            pygame.draw.rect(screen, pygame.Color("black"), (1100, 400, 250, 20), 4)
            stick_man1.dophysics()
            stick_man2.dophysics()



            stick_man1.move(pygame.K_d, pygame.K_a, pygame.K_w,pygame.K_q)
            stick_man1.draw()
            stick_man2.move(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_RALT)
            stick_man2.draw()
            redscore.draw()
            bluescore.draw()




            countdownscreen.draw()
            if tag_counter > 0:
                tag_counter -= 1
                s = pygame.Surface((screen.get_width(),screen.get_height()))  # the size of your rect
                s.set_alpha(200)  # alpha level
                s.fill((0, 0, 0))  # this fills the entire surface
                screen.blit(s, (0, 0))

                screen.blit(tag_image, (screen.get_width() / 2 -tag_image.get_width() / 2 , 150))
            pygame.display.update()




if __name__ == "__main__":
    main()
