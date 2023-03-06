# Wana Game
import math
import random
import pygame
import numpy as np
from copy import deepcopy
from pygame.locals import *
from sys import exit


# Functional Macros
GAME_WIDTH = 9
GAME_HALF = GAME_WIDTH // 2
EMPTY = 0
OUTSIDE = -1



# Display Macros
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SIDE_BORDER = 150
SQUARE_WIDTH = 100
INNER_SQUARE_WIDTH = 90
SQUARE_MARGIN = (SQUARE_WIDTH - INNER_SQUARE_WIDTH) / 2
PIECE_RADIUS = 40


class State:
    
    connections = [
        [(0, 0), (0, 0), (0, 0), (3, 0), (0, 0), (3, 8), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (3, 1), (0, 0), (3, 7), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (3, 2), (0, 0), (3, 6), (0, 0), (0, 0), (0, 0)],
        [(0, 3), (1, 3), (2, 3), (0, 0), (0, 0), (0, 0), (2, 5), (1, 5), (0, 5)],
        [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
        [(8, 3), (7, 3), (6, 3), (0, 0), (0, 0), (0, 0), (6, 5), (7, 5), (8, 5)],
        [(0, 0), (0, 0), (0, 0), (5, 2), (0, 0), (5, 6), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (5, 1), (0, 0), (5, 7), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (5, 0), (0, 0), (5, 8), (0, 0), (0, 0), (0, 0)]
    ]

    def __init__(self, width):
        self.board = [
            [-1, -1, -1, 2, 0, 2, -1, -1, -1],
            [-1, -1, -1, 2, 0, 2, -1, -1, -1],
            [-1, -1, -1, 2, 0, 2, -1, -1, -1],
            [ 0,  0,  0, 2, 0, 2,  0,  0,  0],
            [ 0,  0,  0, 0, 0, 0,  0,  0,  0],
            [ 0,  0,  0, 1, 0, 1,  0,  0,  0],
            [-1, -1, -1, 1, 0, 1, -1, -1, -1],
            [-1, -1, -1, 1, 0, 1, -1, -1, -1],
            [-1, -1, -1, 1, 0, 1, -1, -1, -1]
        ]

        # Quando o jogador tentar andar para -1 trocar o i com o j
        self.player = 1
        self.winner = -1
        self.width = width

    def move(self, moveFrom, moveTo):

        counter_1 = 0
        counter_2 = 0

        new_state = deepcopy(self)
        new_state.board[moveTo[0]][moveTo[1]] = self.board[moveFrom[0]][moveFrom[1]]
        new_state.board[moveFrom[0]][moveFrom[1]] = EMPTY
        new_state.player = 3 - self.player

        
        for i in range(self.width):
            for j in range(self.width):
                if new_state.board[i][j] == 1:
                    counter_1 += 1
                elif new_state.board[i][j] == 2:
                    counter_2 += 1
        
        if counter_1 != 8 or counter_2 != 8:
            print("Move from: ", moveFrom)
            print("Move to: ", moveTo)
            print("Original position: ", self.board[moveFrom[0]][moveFrom[1]])
            print("New position: ", self.board[moveTo[0]][moveTo[1]])
            print("After Move From: ", new_state.board[moveFrom[0]][moveFrom[1]])
            print("After Move To: ", new_state.board[moveTo[0]][moveTo[1]])


        return new_state
    
    def available_moves(self):
        moves = []
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] == self.player:
                    moves += self.available_moves_from((i, j))
        return moves
    
    def available_moves_from(self, pos):
        moves = []
        i, j = pos[0], pos[1]

        # UP
        if self.board[(i-1)][j] == EMPTY:
            moves.append(((i, j), ((i-1), j)))
        elif self.board[(i-1)][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))

        # DOWN
        if self.board[(i+1)%GAME_WIDTH][j] == EMPTY:
            moves.append(((i, j), ((i+1)%GAME_WIDTH, j)))
        elif self.board[(i+1)%GAME_WIDTH][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # LEFT
        if self.board[i][(j-1)] == EMPTY:
            moves.append(((i, j), (i, (j-1))))
        elif self.board[i][(j-1)] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # RIGHT
        if self.board[i][(j+1)%GAME_WIDTH] == EMPTY:
            moves.append(((i, j), (i, (j+1)%GAME_WIDTH)))
        elif self.board[i][(j+1)%GAME_WIDTH] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))

        return moves




class Game:

    def __init__(self):
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
                            

            execute_random_move(self)
            
            # Wait for 1 second
            self.clock.tick(2)


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


def execute_random_move(game):
    (moveFrom, moveTo) = random.choice(game.state.available_moves())
    game.state = game.state.move(moveFrom, moveTo)


def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    if (depth == 0 or state.winner != -1):
        return evaluate_func(state, player)
    if (maximizing):
        value = -math.inf
        for move in state.available_moves:
            value = max(value, minimax(state.move(move), depth - 1, alpha, beta, False, player, evaluate_func))
            alpha = max(alpha, value)
            if (beta <= alpha):
                break
        return value
    else:
        value = math.inf
        for move in state.available_moves:
            value = min(value, minimax(state.move(move), depth - 1, alpha, beta, True, player, evaluate_func))
            beta = min(beta, value)
            if (beta <= alpha):
                break
        return value



game = Game()
game.run()


