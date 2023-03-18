# Class Menu using pygame

import pygame_menu

from ai import *

options = [
    ('Human', 0),
    ('AI Lvl1 - Random', 1),
    ('AI Lvl2 - MinMax 1', 2),
    ('AI Lvl3 - MinMax 2', 3),
    ('AI Lvl4 - MinMax 3', 4),
    ('AI Lvl5 - MinMax 4', 5),
    ('AI Lvl6 - Monte Carlo 10', 6),
    ('AI Lvl7 - Monte Carlo 100', 7),
    ('AI Lvl7 - Monte Carlo 500', 8)
]

class Menu:

    def __init__(self, width, height):
        self.player1 = execute_human_move   
        self.player2 = execute_human_move    
        self.board_number = 0
        self.ready = False
        self.menu = pygame_menu.Menu('Wana Game', width, height, theme=pygame_menu.themes.THEME_DEFAULT) # It's possible to change the theme or even create a new one
        self.menu.add.selector('Player 1 :', options, onchange=self.set_player1)
        self.menu.add.selector('Player 2 :', options, onchange=self.set_player2)
        self.menu.add.selector('Board size :', [('9x9', 0), ('12x12', 1)], onchange=self.set_board_number)
        self.menu.add.button('Play', self.set_ready)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    
    def run(self, screen):
        self.menu.mainloop(screen)
        
    def set_ready(self):
        self.ready = True
        self.menu.disable() # force main loop to exit to move on to the game

    # Probably could have done this in a better way, but i'm not that familiar with this pygame_menu
    def set_player1(self, value, index):
        self.set_player(value, 1)

    def set_player2(self, value, index):
        self.set_player(value, 2)
        
    def set_player(self, value, n_player):
        type_player = value[0][1]
        if (type_player == 0):
            player = execute_human_move
        elif (type_player == 1):
            player = execute_random_move
        elif (type_player == 2):
            player = execute_minimax_move(heuristic_function1, 2)
        elif (type_player == 3):
            player = execute_minimax_move(heuristic_function2, 2)
        elif (type_player == 4):
            player = execute_minimax_move(heuristic_function3, 3)
        elif (type_player == 5):
            player = execute_minimax_move(heuristic_function4, 3)
        elif (type_player == 6):
            player = execute_monte_carlo_move(10)
        elif (type_player == 7):
            player = execute_monte_carlo_move(100)
        elif (type_player == 8):
            player = execute_monte_carlo_move(500)
        else:
            return

        if (n_player == 1):
            self.player1 = player
        else:
            self.player2 = player

        
    def set_board_number(self, value, index):
        self.board_number = value[0][1]
            