# Wana Game
import pygame
from pygame.locals import *
from sys import exit
from board import *




# Display Macros
SIDE_BORDER = 250
UP_BORDER = 100
BOARD_WIDTH = 700
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
        # Draw Players
        font = pygame.font.SysFont("arial", 50)
        color_shade, color_white = (90, 90, 90), (255, 255, 255)
        if self.state.player == 1:
            text1 = font.render("PLAYER 1", True, color_white)
            text2 = font.render("PLAYER 2", True, color_shade)
        else:
            text1 = font.render("PLAYER 1", True, color_shade)
            text2 = font.render("PLAYER 2", True, color_white)

        screen.blit(text1, (SIDE_BORDER + BOARD_WIDTH//2-115, UP_BORDER*1.3 + BOARD_WIDTH))
        screen.blit(text2, (SIDE_BORDER + BOARD_WIDTH//2-115, UP_BORDER*0.4))

        # Draw Square of choosing piece
        if self.human_turn:
            self.draw_square(screen, self.human_move[0], (0, 255, 0), padding=10)
        
        # Draw Square of moving place
        if self.human_move_piece_selected:
            self.draw_square(screen, self.human_move[1], (0, 155, 155), padding=10)

        # Draw Board
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
        
    def draw_game_over(self, screen):
        # Make the background darker
        surface = pygame.Surface((BOARD_WIDTH, BOARD_WIDTH))
        surface.set_alpha(128)
        surface.fill((0, 0, 0))
        screen.blit(surface, (SIDE_BORDER, UP_BORDER))
        
        big_font = pygame.font.SysFont("arial", 100)
        big_text = big_font.render("GAME OVER", True, (255, 255, 255))
        
        small_font = pygame.font.SysFont("arial", 50)
        small_text = small_font.render("Player " + str(self.state.winner) + " won the game!", True, (255, 255, 255))

        screen.blit(big_text, (SIDE_BORDER + BOARD_WIDTH//2-300, UP_BORDER + BOARD_WIDTH//2-50))
        screen.blit(small_text, (SIDE_BORDER + BOARD_WIDTH//2-260, UP_BORDER + BOARD_WIDTH//2+50))



        