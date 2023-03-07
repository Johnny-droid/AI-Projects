# Wana Game
import pygame
import numpy as np
from copy import deepcopy
from pygame.locals import *
from sys import exit
from ai import *
from board import *


# Display Macros
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SIDE_BORDER = 150
SQUARE_WIDTH = 100
INNER_SQUARE_WIDTH = 90
SQUARE_MARGIN = (SQUARE_WIDTH - INNER_SQUARE_WIDTH) / 2
PIECE_RADIUS = 40


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.state = State(GAME_WIDTH)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.init()
        pygame.display.set_caption("Wana Game")

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    # Press P to pause
                    if event.key == K_p:
                        done = False
                        while not done:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_p:
                                        done = True
                            
            if self.state.player == 1:
                self.player1(self)
            else:
                self.player2(self)

            if self.state.winner != -1:
                print("Player", self.state.winner, "wins!")
                break

            # Wait for 1 second
            # self.clock.tick(1)


            self.screen.fill((0, 0, 0))
            self.draw_game()
            pygame.display.update()




    def draw_game(self):
        for i in range(self.state.width):
            for j in range(self.state.width):
                if self.state.board[i][j] == -1:
                    self.draw_square((i, j), (50, 50, 50))
                elif self.state.board[i][j] == 0:
                    self.draw_square((i, j), (255, 255, 255))
                elif self.state.board[i][j] == 1:
                    self.draw_square((i, j), (255, 0, 0))
                elif self.state.board[i][j] == 2:
                    self.draw_square((i, j), (0, 0, 255))

    def draw_square(self, pos, color):
        pygame.draw.rect(self.screen, color, 
            (SIDE_BORDER + pos[1] * SQUARE_WIDTH + SQUARE_MARGIN, 
             pos[0] * SQUARE_WIDTH + SQUARE_MARGIN, 
             INNER_SQUARE_WIDTH, INNER_SQUARE_WIDTH))





#game = Game(execute_random_move, execute_random_move)
#game = Game(execute_random_move, execute_minimax_move(heuristic_function1, 4))
#game = Game(execute_random_move, execute_minimax_move(heuristic_function4, 3))
game = Game(execute_minimax_move(heuristic_function2, 3), execute_minimax_move(heuristic_function4, 4))
game.run()


