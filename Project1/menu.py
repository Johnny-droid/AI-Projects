# Class Menu using pygame

import pygame
import pygame_menu

from ai import *


class Menu:

    def __init__(self):
        self.player1 = 1    # Change this into default human player
        self.player2 = 1
        self.ready = False
        self.menu = pygame_menu.Menu('Wana Game', 1200, 1000)
        self.menu.add.selector('Player 1 :', [('Human', 1), ('AI Lvl1', 2), ('AI Lvl2', 2), ('AI Lvl3', 3), ('AI Lvl4', 4)], onchange=self.set_player1)
        self.menu.add.selector('Player 2 :', [('Human', 1), ('AI Lvl1', 2), ('AI Lvl2', 2), ('AI Lvl3', 3), ('AI Lvl4', 4)], onchange=self.set_player2)
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
        if (type_player == 2):
            player = execute_random_move
        elif (type_player == 3):
            player = execute_minimax_move(heuristic_function1, 4)
        elif (type_player == 4):
            player = execute_minimax_move(heuristic_function2, 4)

        if (n_player == 1):
            self.player1 = player
        else:
            self.player2 = player

        


    def draw(self, screen):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()
        
        # Display the letters menu
        font = pygame.font.SysFont("comicsansms", 100)
        text = font.render("Menu", True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 90, screen_height / 2 - 100))

        # Create a button
        button = pygame.Rect(screen_width / 2 - 100, screen_height / 2, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), button)

        # The button is clicked
        if button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                print("Button clicked")