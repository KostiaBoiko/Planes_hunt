import pygame
from settings import *
from game import *

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Z-Plane Hunt')
        self.menuscreen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.start_button = pygame.transform.scale(pygame.image.load('assets/menu/button_StartGame.png').convert_alpha(),
                                              [256, 83])
        self.start_button_rect = self.start_button.get_rect(topleft=(232, 60))
        self.settings_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Settings.png').convert_alpha(),
                                                 [204, 57])
        self. settings_button_rect = self.settings_button.get_rect(topleft=(258, 200))
        self.exit_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Exit.png').convert_alpha(),
                                             [204, 57])
        self.exit_button_rect = self.exit_button.get_rect(topleft=(258, 300))

        self.bg = pygame.transform.scale(pygame.image.load('assets/menu/background.png').convert_alpha(), [720, 480])

    def start_menu(self):
        menu_running = True
        while menu_running:
            self.menuscreen.blit(self.bg, (0, 0))
            self.menuscreen.blit(self.start_button, self.start_button_rect)
            self.menuscreen.blit(self.settings_button, self.settings_button_rect)
            self.menuscreen.blit(self.exit_button, self.exit_button_rect)

            mouse = pygame.mouse.get_pos()
            if self.start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                game = Game()
                game.run()

            elif self.settings_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.setting_123(game)
                game.settings_12345 = 1

            elif self.exit_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():  # получаємо список всіх можливих подій
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()







