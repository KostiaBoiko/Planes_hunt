import pygame
import settings
import sys
import enemy
from random import randint


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.RESOLUTION, flags=pygame.SCALED)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Z-Plane Hunt')
        self.mouse = 0, 0
        self.timer = 60

        self.background = pygame.image.load('assets/game/game_back.png')
        self.score_bar = pygame.image.load('assets/game/score_bar.png')
        self.cursor = pygame.image.load('assets/game/scope.png')
        self.font = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 35)

        pygame.mouse.set_visible(0)
        self.animation_timer = 60
        self.is_mouse_pressed = False
        self.score = 0

        self.score_bar_text = self.font.render(f"Score: {self.score}", False, "White")

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
    def gameplay(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            enemy.Enemy(self)
            self.timer = randint(30, 50)

        # updating model position
        for target in enemy.enemies:
            target.update(self)

        # drawing the model
        for target in enemy.enemies:
            target.draw(self)

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.gameplay()
            self.refresh()