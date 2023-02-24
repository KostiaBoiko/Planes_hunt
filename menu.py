from pygame import *

MenuFont = font.SysFont('arial', 50)

class Menu:
    def __init__(self):
        self._option_surfaces = [] # список поверхонь з текстом
        self._callbacks = [] # список з функціями
        self._current_option_index = 0 # поточно вибрана функція

    def append_option(self, option, callback):
        self._option_surfaces.append(MenuFont.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)
