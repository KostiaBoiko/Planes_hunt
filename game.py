import pygame
import settings
import sys
import enemy
from random import randint

class Game:
    def __init__(self):
        self.game_running = None
        self.screen = pygame.display.set_mode(settings.RESOLUTION, flags=pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.mouse = 0, 0
        self.timer = 60

        self.background = pygame.image.load('assets/game/game_back.png')
        self.score_bar = pygame.image.load('assets/game/score_bar.png')
        self.cursor = pygame.image.load('assets/game/scope.png')
        pygame.font.init()
        self.font = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 35)

        self.animation_timer = 60
        self.is_mouse_pressed = False
        self.score = 0
        self.max_score = 0
        self.game_mode = 0

        self.score_bar_text = self.font.render(f"Score: {self.score}", False, "White")
        self.menu_button = pygame.transform.scale(pygame.image.load('assets/menu/menu_button.png').convert_alpha(),
                                                  [50, 50])
        self.menu_button_rect = self.menu_button.get_rect(topleft=(10, 420))

        pygame.mixer.init()
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.mp3")
        self.explosion_sound.set_volume(0.15)
        self.lose_sound = pygame.mixer.Sound("assets/sounds/fail.mp3")
        self.lose_sound.set_volume(0.2)
        self.frog_sound = pygame.mixer.Sound("assets/sounds/frog-sound.mp3")
        self.frog_sound.set_volume(0.05)


    def refresh(self, menu):
        pygame.display.flip()
        self.clock.tick(settings.FPS)
        self.mouse = pygame.mouse.get_pos()
        self.score_bar_text = self.font.render(f"Score: {self.score}", True, "White")
        if self.menu_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
            menu.click.play()
            self.run_menu(menu)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.score_bar, (settings.WIDTH - 188, settings.HEIGHT - 64))
        self.screen.blit(self.score_bar_text, (settings.WIDTH - 170, settings.HEIGHT - 42))
        self.screen.blit(self.cursor, self.mouse)
        self.screen.blit(self.menu_button, self.menu_button_rect)

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def gameplay(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            enemy.Enemy(self)
            if self.game_mode == -1:
                self.timer = randint(60, 100)
            elif self.game_mode == 1:
                self.timer = randint(5, 20)
            else:
                self.timer = randint(20, 50)


        # updating model position
        for target in enemy.enemies:
            target.update(self)

        # drawing the model
        for target in enemy.enemies:
            target.draw(self)

    def check_score(self, menu):
        if self.score > self.max_score:
            self.max_score = self.score
        if self.score < 0:
            self.lose_sound.play()
            self.frog_sound.play()
            self.run_menu(menu)

    def run_menu(self, menu):
        menu.bg_music.stop()
        self.score = 0
        enemy.enemies.clear()
        self.game_running = False
        menu.menu(self)


    def run(self, menu):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.check_score(menu)
            self.draw()
            self.gameplay()
            self.refresh(menu)
