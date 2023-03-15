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

# Assets
EMPTY_SLOT_IMG = pygame.image.load("assets/E_Slot.png")
PLAYER_1_IMG = pygame.image.load("assets/1_Player.png")
PLAYER_2_IMG = pygame.image.load("assets/2_Player.png")
VER_CONNECTOR_IMG = pygame.image.load("assets/V_Connector.png")
HOR_CONNECTOR_IMG = pygame.image.load("assets/H_Connector.png")
BRIDGE_1_IMG = pygame.image.load("assets/1_Bridge.png")
BRIDGE_2_IMG = pygame.image.load("assets/2_Bridge.png")
BRIDGE_3_IMG = pygame.image.load("assets/3_Bridge.png")
BRIDGE_4_IMG = pygame.image.load("assets/4_Bridge.png")
SELECTED_SLOT_P1_IMG = pygame.image.load("assets/Slot_Select_P1.png")
SELECTED_SLOT_P2_IMG = pygame.image.load("assets/Slot_Select_P2.png")
POSSIBLE_SLOT_IMG = pygame.image.load("assets/Slot_Possible.png")
MOVE_SLOT_IMG = pygame.image.load("assets/Slot_Move.png")
BOARD_TEXTURE_IMG = pygame.image.load("assets/Board_Texture.png")

IMGS = [EMPTY_SLOT_IMG, PLAYER_1_IMG, PLAYER_2_IMG, VER_CONNECTOR_IMG, HOR_CONNECTOR_IMG, BRIDGE_1_IMG, BRIDGE_2_IMG, BRIDGE_3_IMG, BRIDGE_4_IMG]


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

        screen.blit(text1, (SIDE_BORDER, UP_BORDER*0.4))
        screen.blit(text2, (BOARD_WIDTH + SIDE_BORDER - BOARD_WIDTH//3 , UP_BORDER*0.4))


        # Draw Board
        for i in range(self.state.width):
            for j in range(self.state.width):
                self.draw_image(screen, (i, j), BOARD_TEXTURE_IMG)
        for i in range(self.state.width):
            for j in range(self.state.width):
                self.draw_image(screen, (i, j), IMGS[self.state.vboard[i][j]])

        # Draw Square of choosing piece
        if self.human_turn:
            if self.state.player == 1:
                self.draw_image(screen, self.human_move[0], SELECTED_SLOT_P1_IMG)
            elif self.state.player == 2:
                self.draw_image(screen, self.human_move[0], SELECTED_SLOT_P2_IMG)

        # Draw Moving Options
        if self.human_move_piece_selected:
            for move in self.state.available_moves_from(self.human_move[0]):
                self.draw_image(screen, move[1], POSSIBLE_SLOT_IMG)      

        # Draw Square of moving place
        if self.human_move_piece_selected:
            self.draw_image(screen, self.human_move[1], MOVE_SLOT_IMG)


    def draw_square(self, screen, pos, color, padding=0):
        pygame.draw.rect(screen, color, 
            (SIDE_BORDER + pos[1] * self.square_width + self.square_margin - padding/2, 
             UP_BORDER + pos[0] * self.square_width + self.square_margin - padding/2, 
             self.inner_square_width + padding, self.inner_square_width + padding))
        
    def draw_image(self, screen, pos, image):
        resized_image = pygame.transform.scale(image, (int(self.square_width)+1, int(self.square_width)+1))
        screen.blit(resized_image, (SIDE_BORDER + pos[1] * self.square_width, 
                            UP_BORDER + pos[0] * self.square_width))
        

    def draw_game_over(self, screen):
        # Make the background darker
        surface = pygame.Surface((BOARD_WIDTH, BOARD_WIDTH))
        surface.set_alpha(128)
        surface.fill((0, 0, 0))
        screen.blit(surface, (SIDE_BORDER, UP_BORDER))
        
        big_font = pygame.font.SysFont("arial", 70)
        big_text = big_font.render("GAME OVER", True, (255, 255, 255))
        
        small_font = pygame.font.SysFont("arial", 30)
        small_text = small_font.render("Player " + str(self.state.winner) + " won the game!", True, (255, 255, 255))

        screen.blit(big_text, (SIDE_BORDER + BOARD_WIDTH//2-220, UP_BORDER + BOARD_WIDTH+5))
        screen.blit(small_text, (SIDE_BORDER + BOARD_WIDTH//2-160, UP_BORDER + BOARD_WIDTH+65))


    def draw_pause(self, screen):
        # Make the background darker
        surface = pygame.Surface((BOARD_WIDTH, BOARD_WIDTH))
        surface.set_alpha(128)
        surface.fill((0, 0, 0))
        screen.blit(surface, (SIDE_BORDER, UP_BORDER))

        big_font = pygame.font.SysFont("arial", 100)
        big_text = big_font.render("PAUSE", True, (255, 255, 255))

        screen.blit(big_text, (SIDE_BORDER + BOARD_WIDTH//2-170, UP_BORDER + BOARD_WIDTH//2-50))
        