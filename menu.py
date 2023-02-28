import pygame
from settings import *
from game import *

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Z-Plane Hunt')
        self.menuscreen = pygame.display.set_mode(settings.RESOLUTION, flags=pygame.SCALED)
        self.bg = pygame.transform.scale(pygame.image.load('assets/menu/background.png').convert_alpha(), [720, 480])

        # -------------------------------------------menu buttons----------------------------------------
        self.start_button = pygame.transform.scale(pygame.image.load('assets/menu/button_StartGame.png').convert_alpha(),
                                              [256, 83])
        self.start_button_rect = self.start_button.get_rect(topleft=(232, 50))
        self.settings_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Settings.png').convert_alpha(),
                                                 [204, 57])
        self.settings_button_rect = self.settings_button.get_rect(topleft=(258, 260))
        self.exit_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Exit.png').convert_alpha(),
                                             [204, 57])
        self.exit_button_rect = self.exit_button.get_rect(topleft=(258, 360))

        #-------------------------------------------settings buttons----------------------------------------
        self.easymode_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Easymode.png').convert_alpha(),
            [204, 57])
        self.easymode_button_rect = self.easymode_button.get_rect(topleft=(258, 40))

        self.normalmode_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Normalmode.png').convert_alpha(),
            [204, 57])
        self.normalmode_button_rect = self.normalmode_button.get_rect(topleft=(258, 120))

        self.hardmode_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Hardmode.png').convert_alpha(),
                                             [204, 57])
        self.hardmode_button_rect = self.hardmode_button.get_rect(topleft=(258, 200))

        self.back_button = pygame.transform.scale(pygame.image.load('assets/menu/button_Back.png').convert_alpha(),
                                                  [204, 57])
        self.back_button_rect = self.back_button.get_rect(topleft=(500, 360))

        self.bg_music = pygame.mixer.Sound('assets/sounds/undertale_050. Metal Crusher.mp3')
        self.bg_music.play()


    def play_song(self, game):
        self.bg_music.stop()
        if game.game_mode == -1:
            self.bg_music = pygame.mixer.Sound('assets/sounds/Hatsune Miku - Ievan Polkka (mp3store.cc).mp3')
            self.bg_music.play()
        elif game.game_mode == 1:
            self.bg_music = pygame.mixer.Sound(
                'assets/sounds/Daniel_Tidwell_-_At_Dooms_Gate_DOOM_E1M1_(musmore.com).mp3')
            self.bg_music.play()
        elif game.game_mode == 0:
            self.bg_music = pygame.mixer.Sound('assets/sounds/undertale_050. Metal Crusher.mp3')
            self.bg_music.play()


    def draw_menu(self):
        self.menuscreen.blit(self.bg, (0, 0))
        self.menuscreen.blit(self.start_button, self.start_button_rect)
        self.menuscreen.blit(self.settings_button, self.settings_button_rect)
        self.menuscreen.blit(self.exit_button, self.exit_button_rect)

    def draw_settings(self):
        self.menuscreen.blit(self.bg, (0, 0))
        self.menuscreen.blit(self.easymode_button, self.easymode_button_rect)
        self.menuscreen.blit(self.normalmode_button, self.normalmode_button_rect)
        self.menuscreen.blit(self.hardmode_button, self.hardmode_button_rect)
        self.menuscreen.blit(self.back_button, self.back_button_rect)

    def settings(self, game):
        pygame.mouse.set_visible(1)
        settings_running = True
        self.draw_settings()
        while settings_running:
            mouse = pygame.mouse.get_pos()
            if self.easymode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                game.game_mode = -1


            elif self.normalmode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                game.game_mode = 0


            elif self.hardmode_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                game.game_mode = 1


            elif self.back_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.start_menu(game)
                settings_running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def start_menu(self, game):
        pygame.mouse.set_visible(1)
        menu_running = True
        self.draw_menu()
        while menu_running:
            mouse = pygame.mouse.get_pos()
            if self.start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.play_song(game)
                pygame.mouse.set_visible(0)
                menu_running = False
                game.run(self)

            elif self.settings_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                menu_running = False
                self.settings(game)


            elif self.exit_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
