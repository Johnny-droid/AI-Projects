# Wana Game
import pygame
from pygame.locals import *
from sys import exit
from board import *


# Display Macros
SIDE_BORDER = 150
UP_BORDER = 50
BOARD_WIDTH = 900
INNER_SQUARE_WIDTH_PERCENTAGE = 0.9


class Game:

    def __init__(self, player1, player2, board_number):
        self.player1 = player1
        self.player2 = player2
        self.state = State(board_number)
        self.clock = pygame.time.Clock()
        self.square_width = BOARD_WIDTH / self.state.width
        self.inner_square_width = self.square_width * INNER_SQUARE_WIDTH_PERCENTAGE
        self.square_margin = (self.square_width - self.inner_square_width) / 2


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
            (SIDE_BORDER + pos[1] * self.square_width + self.square_margin, 
             UP_BORDER + pos[0] * self.square_width + self.square_margin, 
             self.inner_square_width, self.inner_square_width))



