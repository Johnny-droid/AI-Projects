# Wana Game
import pygame
from pygame.locals import *
from sys import exit
from board import *


# Display Macros
SIDE_BORDER = 150
UP_BORDER = 50
SQUARE_WIDTH = 100
INNER_SQUARE_WIDTH = 90
SQUARE_MARGIN = (SQUARE_WIDTH - INNER_SQUARE_WIDTH) / 2
PIECE_RADIUS = 40


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.state = State(GAME_WIDTH)
        self.clock = pygame.time.Clock()

    def player_move(self):
        if self.state.player == 1:
            self.player1(self)
        else:
            self.player2(self)

    def get_winner(self):
        return self.state.winner


    def draw(self, screen):
        for i in range(self.state.width):
            for j in range(self.state.width):
                if self.state.board[i][j] == -1:
                    self.draw_square(screen, (i, j), (50, 50, 50))
                elif self.state.board[i][j] == 0:
                    self.draw_square(screen, (i, j), (255, 255, 255))
                elif self.state.board[i][j] == 1:
                    self.draw_square(screen, (i, j), (255, 0, 0))
                elif self.state.board[i][j] == 2:
                    self.draw_square(screen, (i, j), (0, 0, 255))

    def draw_square(self, screen, pos, color):
        pygame.draw.rect(screen, color, 
            (SIDE_BORDER + pos[1] * SQUARE_WIDTH + SQUARE_MARGIN, 
             UP_BORDER + pos[0] * SQUARE_WIDTH + SQUARE_MARGIN, 
             INNER_SQUARE_WIDTH, INNER_SQUARE_WIDTH))





#game = Game(execute_random_move, execute_random_move)
#game = Game(execute_random_move, execute_minimax_move(heuristic_function1, 4))
#game = Game(execute_random_move, execute_minimax_move(heuristic_function4, 3))
#game = Game(execute_minimax_move(heuristic_function2, 3), execute_minimax_move(heuristic_function4, 4))
#game.run()


