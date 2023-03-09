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
        self.square_width = BOARD_WIDTH / self.state.width
        self.inner_square_width = self.square_width * INNER_SQUARE_WIDTH_PERCENTAGE
        self.square_margin = (self.square_width - self.inner_square_width) / 2
        self.human_turn = False
        self.human_move = [(self.state.width // 2, self.state.width // 2), (self.state.width // 2, self.state.width // 2)]
        self.human_move_piece_selected = False

    def player_move(self, key):
        if self.state.player == 1:
            self.player1(self, key)
        else:
            self.player2(self, key)

    def get_winner(self):
        return self.state.winner


    def draw(self, screen):
        if self.human_turn:
            self.draw_square(screen, self.human_move[0], (0, 255, 0), padding=10)
        
        if self.human_move_piece_selected:
            self.draw_square(screen, self.human_move[1], (0, 155, 155), padding=10)

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

    def draw_square(self, screen, pos, color, padding=0):
        pygame.draw.rect(screen, color, 
            (SIDE_BORDER + pos[1] * self.square_width + self.square_margin - padding/2, 
             UP_BORDER + pos[0] * self.square_width + self.square_margin - padding/2, 
             self.inner_square_width + padding, self.inner_square_width + padding))



        