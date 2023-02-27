from pygame import *
from game import *
from menu import *
from settings import  *
from menu import *

if __name__ == '__main__':
    game = Game()
    menu = Menu()
    menu.start_menu(game)


