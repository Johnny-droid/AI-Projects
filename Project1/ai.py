import math
import random
from pygame.locals import *

# HUMAN MOVE
def execute_human_move(game, key=None):
    game.human_turn = True
    if key == None:
        return

    game.human_turn = True
    # Decide which piece to move
    if (not game.human_move_piece_selected):

        if key == K_UP:
            game.human_move[0] = ((game.human_move[0][0] - 1)%game.state.width, game.human_move[0][1])
        elif key == K_DOWN:
            game.human_move[0] = ((game.human_move[0][0] + 1)%game.state.width , game.human_move[0][1])
        elif key == K_LEFT:
            game.human_move[0] = (game.human_move[0][0], (game.human_move[0][1] - 1)%game.state.width)
        elif key == K_RIGHT:
            game.human_move[0] = (game.human_move[0][0], (game.human_move[0][1] + 1)%game.state.width)
        elif key == K_SPACE and game.state.board[game.human_move[0][0]][game.human_move[0][1]] == game.state.player:
            game.human_move[1] = game.human_move[0]
            game.human_move_piece_selected = True
        
        
    # Decide where to move the piece
    else:

        if key == K_UP:
            game.human_move[1] = (game.human_move[1][0] - 1, game.human_move[1][1])
        elif key == K_DOWN:
            game.human_move[1] = ((game.human_move[1][0] + 1)%game.state.width , game.human_move[1][1])
        elif key == K_LEFT:
            game.human_move[1] = (game.human_move[1][0], game.human_move[1][1] - 1)
        elif key == K_RIGHT:
            game.human_move[1] = (game.human_move[1][0], (game.human_move[1][1] + 1)%game.state.width)

        elif key == K_SPACE and (game.human_move[1] != game.human_move[0]) and (tuple(game.human_move) in game.state.available_moves_from(game.human_move[0])):
            game.state = game.state.move(game.human_move[0], game.human_move[1])
            game.human_move[0] = game.human_move[1]
            game.human_move_piece_selected = False
            game.human_turn = False

        

            


def heuristic_function1(state, player):
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == player:
                counter += len(state.available_moves_from((i, j)))
    return counter

def heuristic_function2(state, player):
    opponent = 3 - player
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == opponent:
                counter -= len(state.available_moves_from((i, j)))
    return counter

def heuristic_function3(state, player):
    return heuristic_function1(state, player) + heuristic_function2(state, player)

def heuristic_function4(state, player):
    opponent = 3 - player
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == player:
                moves = len(state.available_moves_from((i, j)))
                if moves == 0:
                    counter -= 100
                elif moves == 1:
                    counter -= 10
            
            if state.board[i][j] == opponent:
                moves = len(state.available_moves_from((i, j)))
                if moves == 0:
                    counter += 100
                elif moves == 1:
                    counter += 10
    return counter




def execute_random_move(game, key=None):
    (moveFrom, moveTo) = random.choice(game.state.available_moves())
    game.state = game.state.move(moveFrom, moveTo)

def execute_minimax_move(evaluate_func, depth):
    def minimax_move(game, key=None):
        best_move = None
        best_value = -math.inf
        for move in game.state.available_moves(): # move = ((i, j), (i', j'))
            value = minimax(game.state.move(move[0], move[1]), depth - 1, -math.inf, math.inf, False, game.state.player, evaluate_func)
            if (value > best_value):
                best_value = value
                best_move = move
        game.state = game.state.move(best_move[0], best_move[1])
    return minimax_move

def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    if (depth == 0 or state.winner != -1):
        return evaluate_func(state, player)
    if (maximizing):
        value = -math.inf
        for move in state.available_moves():
            value = max(value, minimax(state.move(move[0], move[1]), depth - 1, alpha, beta, False, player, evaluate_func))
            alpha = max(alpha, value)
            if (beta <= alpha):
                break
        return value
    else:
        value = math.inf
        for move in state.available_moves():
            value = min(value, minimax(state.move(move[0], move[1]), depth - 1, alpha, beta, True, player, evaluate_func))
            beta = min(beta, value)
            if (beta <= alpha):
                break
        return value