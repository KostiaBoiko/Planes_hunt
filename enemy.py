from random import randint, choice, uniform
from game import *
from settings import *
import pygame

# Текстури літака який летить вправо
plane_textures_right = [pygame.image.load('assets/game/plane_1.png'),
                        pygame.transform.flip(pygame.image.load('assets/game/plane_2.png'), True, False),
                        pygame.transform.flip(pygame.image.load('assets/game/plane_3.png'), True, False),
                        ]
# Текстури літака який летить вліво
plane_textures_left = [pygame.transform.flip(pygame.image.load('assets/game/plane_1.png'), True, False),
                       pygame.image.load('assets/game/plane_2.png'),
                       pygame.image.load('assets/game/plane_3.png'),
                       ]
# Текстури вибуху
explosion_texture = [pygame.transform.scale(pygame.image.load('assets/game/explosion/explosion_1.png'), [50, 50]),
                     pygame.transform.scale(pygame.image.load('assets/game/explosion/explosion_2.png'), [50, 50]),
                     pygame.transform.scale(pygame.image.load('assets/game/explosion/explosion_3.png'), [50, 50]),
                     pygame.transform.scale(pygame.image.load('assets/game/explosion/explosion_4.png'), [50, 50]),
                     ]
# Список ворогів
enemies = []


class Enemy:
    # Ініціалізація ворога
    def __init__(self, game):
        # Вибір сторони, куди направлений
        self.right_side = choice([True, False])
        # Вибір типу літака
        self.plane_type = randint(0, 2)
        # Вибір швидкості літака
        self.speed = randint(3, 6)
        # Вибір розміру літака
        self.size_multiplier = uniform(0.5, 1)
        # В залежності від напрямку генерування текстури та місця появи літака
        if self.right_side:
            self.x, self.y = -150, randint(-50, 200)
            self.enemy_texture = pygame.transform.scale_by(plane_textures_right[self.plane_type], self.size_multiplier)
        else:
            self.x, self.y = WIDTH, randint(-50, 200)
            self.speed = -self.speed
            self.enemy_texture = pygame.transform.scale_by(plane_textures_left[self.plane_type], self.size_multiplier)
        # Малювання літака
        game.screen.blit(self.enemy_texture, (self.x, self.y))
        # Генерування області колізії літака
        self.enemy_rect = self.enemy_texture.get_rect(topleft=(self.x, self.y))
        # Додавання до списку ворогів нового літака
        enemies.append(self)

    # Перевірка на перетинання літаком кордону
    def check_border(self, game):
        if self.enemy_rect.topleft[0] > WIDTH and self.right_side:
            return self.reduce_points(game)
        elif self.enemy_rect.topleft[0] < -250 and not self.right_side:
            return self.reduce_points(game)

    # Зменшення кількості балів
    def reduce_points(self, game):
        # Видалення ворога зі списку
        enemies.remove(self)
        game.score -= 1

    # Зміна положення літака
    def change_position(self):
        self.x += self.speed
        return self.x

    # Перевірка натисканя на літак
    def check_mouse_collide(self, game):
        if self.enemy_rect.collidepoint(game.mouse) and pygame.mouse.get_pressed()[0]:
            for texture in explosion_texture:
                game.screen.blit(pygame.transform.scale_by(texture, self.size_multiplier),
                                                          (game.mouse[0]-13, game.mouse[1]-13))
            game.explosion_sound.play()
            enemies.remove(self)
            game.score += 1

    # Оновлення всіх параметрів ворога
    def update(self, game):
        self.x = self.enemy_rect.x = self.change_position()
        self.check_border(game)
        self.check_mouse_collide(game)

    # Малювання ворога
    def draw(self, game):
        return game.screen.blit(self.enemy_texture, self.enemy_rect)
