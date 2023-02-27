import pygame
import settings
import sys
import enemy
from random import randint
import menu
import main

class Game:
    def __init__(self):
        #pygame.init()
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

        self.score_bar_text = self.font.render(f"Score: {self.score}", False, "White")

        pygame.mixer.init()
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/vzryv-granaty-rfv.mp3")
        self.explosion_sound.set_volume(0.05)
        self.lose_sound = pygame.mixer.Sound("assets/sounds/fail.mp3")
        self.lose_sound.set_volume(0.1)


    def refresh(self):
        pygame.display.flip()
        self.clock.tick(settings.FPS)
        self.mouse = pygame.mouse.get_pos()
        self.score_bar_text = self.font.render(f"Score: {self.score}", True, "White")

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.score_bar, (settings.WIDTH - 188, settings.HEIGHT - 64))
        self.screen.blit(self.score_bar_text, (settings.WIDTH - 170, settings.HEIGHT - 42))
        self.screen.blit(self.cursor, self.mouse)

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def gameplay(self, ):
        if self.timer > 0:
            self.timer -= 1
        else:
            enemy.Enemy(self)
            self.timer = randint(60, 90)


        # updating model position
        for target in enemy.enemies:
            target.update(self)

        # drawing the model
        for target in enemy.enemies:
            target.draw(self)

    def check_score(self, menu):
        if self.score < 0:
            self.lose_sound.play()
            menu.start_menu(self)
            self.game_running = False
            enemy.enemies.clear()
            self.score = 0


    def run(self, menu):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.check_score(menu)
            self.draw()
            self.gameplay()
            self.refresh()
