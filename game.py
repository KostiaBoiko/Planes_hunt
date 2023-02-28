import pygame
import settings
import sys
import enemy
from random import randint


class Game:
    # Ініціалізація гри
    def __init__(self):
        self.game_running = None
        # Ініціалізація дісплею
        self.screen = pygame.display.set_mode(settings.RESOLUTION, flags=pygame.SCALED)
        # Ініціалізація годиннику
        self.clock = pygame.time.Clock()
        # Ініціалізація миші
        self.mouse = 0, 0
        # Ініціалізація таймеру
        self.timer = 60

        # Ініціалізація зображення для фону
        self.background = pygame.image.load('assets/game/game_back.png')
        # Ініціалізація місця під бали
        self.score_bar = pygame.image.load('assets/game/score_bar.png')
        # Ініціалізація зображення для курсору
        self.cursor = pygame.image.load('assets/game/scope.png')
        # Ініціалізація шрифту
        pygame.font.init()
        # Ініціалізація шрифту для балів
        self.game_font = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 35)

        # Ініціалізація змінної для таймеру
        self.animation_timer = 60

        # Ініціалізація змінної для балів
        self.score = 0
        # Ініціалізація змінної для максимальної кількості балів
        self.max_score = 0
        # Ініціалізація змінної для режиму гри
        self.game_mode = 0

        # Ініціалізація тексту для балів
        self.score_bar_text = self.game_font.render(f"Score: {self.score}", False, "White")
        # Ініціалізація кнопки переходу в меню
        self.menu_button = pygame.transform.scale(pygame.image.load('assets/menu/menu_button.png').convert_alpha(),
                                                  [50, 50])
        self.menu_button_rect = self.menu_button.get_rect(topleft=(10, 420))

        # Ініціалізація звуків
        pygame.mixer.init()
        # Ініціалізація звуку вибуху
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.mp3")
        self.explosion_sound.set_volume(0.15)
        # Ініціалізація звуку програшу
        self.lose_sound = pygame.mixer.Sound("assets/sounds/fail.mp3")
        self.lose_sound.set_volume(0.2)
        # Ініціалізація звуку натискання клавіш
        self.frog_sound = pygame.mixer.Sound("assets/sounds/frog-sound.mp3")
        self.frog_sound.set_volume(0.05)

    # Функція оновлення зображень на екрані
    def refresh(self, menu):
        # Оновлення діспею
        pygame.display.flip()
        # Оновлення встановлення кількості кадрів
        self.clock.tick(settings.FPS)
        # Оновлення позиції миші
        self.mouse = pygame.mouse.get_pos()
        # Генерування відображення балів
        self.score_bar_text = self.game_font.render(f"Score: {self.score}", True, "White")
        # Натискання на кнопку меню
        self.menu_button_pressed(menu)

    # Перевірка натискання на кнопку переходу в меню
    def menu_button_pressed(self, menu):
        if self.menu_button_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
            menu.click.play()
            self.run_menu(menu)

    # Функція "малювання" на діспеї
    def draw(self):
        # Відображення фону
        self.screen.blit(self.background, (0, 0))
        # Відображення вікна з кількістю балів
        self.screen.blit(self.score_bar, (settings.WIDTH - 188, settings.HEIGHT - 64))
        # Відображення кількості балів
        self.screen.blit(self.score_bar_text, (settings.WIDTH - 170, settings.HEIGHT - 42))
        # Відображення курсору
        self.screen.blit(self.cursor, self.mouse)
        # Відображення кнопки меню
        self.screen.blit(self.menu_button, self.menu_button_rect)

    # Перевірка натискання клавіш та закривання вікна
    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Функція гри
    def gameplay(self):
        # Робота таймеру
        if self.timer > 0:
            self.timer -= 1
        else:
            # Появлення ворогів залежно від таймеру
            enemy.Enemy(self)
            if self.game_mode == -1:
                self.timer = randint(60, 100)
            elif self.game_mode == 1:
                self.timer = randint(5, 20)
            else:
                self.timer = randint(20, 50)

        # Оновлення позиції ворогів
        for target in enemy.enemies:
            target.update(self)

        # Малювання ворогів
        for target in enemy.enemies:
            target.draw(self)

    # Перевірка кількості балів
    def check_score(self, menu):
        if self.score > self.max_score:
            self.max_score = self.score
        if self.score < 0:
            self.lose_sound.play()
            self.frog_sound.play()
            self.run_menu(menu)

    # Функція запуску меню
    def run_menu(self, menu):
        menu.bg_music.stop()
        self.score = 0
        enemy.enemies.clear()
        self.game_running = False
        menu.menu(self)

    # Функція яка запускає всі інші
    def run(self, menu):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.check_score(menu)
            self.draw()
            self.gameplay()
            self.refresh(menu)
