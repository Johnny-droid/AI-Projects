import math
import random
import time
from pygame.locals import *


# HUMAN MOVE ============================================================================================================
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
            game.human_move[1] = ((game.human_move[1][0] - 1)%game.state.width, game.human_move[1][1])
        elif key == K_DOWN:
            game.human_move[1] = ((game.human_move[1][0] + 1)%game.state.width , game.human_move[1][1])
        elif key == K_LEFT:
            game.human_move[1] = (game.human_move[1][0], (game.human_move[1][1] - 1)%game.state.width)
        elif key == K_RIGHT:
            game.human_move[1] = (game.human_move[1][0], (game.human_move[1][1] + 1)%game.state.width)

        elif key == K_SPACE and (game.human_move[1] != game.human_move[0]) and (tuple(game.human_move) in game.state.available_moves_from(game.human_move[0])):
            game.state = game.state.move(game.human_move[0], game.human_move[1])
            game.human_move[0] = game.human_move[1]
            game.human_move_piece_selected = False
            game.human_turn = False
        elif key == K_ESCAPE:
            game.human_move_piece_selected = False

        

            
# MINMAX MOVE ============================================================================================================

def heuristic_function1(state, player):
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == player:
                counter += len(state.directions_available_from((i, j)))
    return counter

def heuristic_function2(state, player):
    opponent = 3 - player
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == opponent:
                counter -= len(state.directions_available_from((i, j)))
    return counter

def heuristic_function3(state, player):
    return heuristic_function1(state, player) + heuristic_function2(state, player)

def heuristic_function4(state, player):
    opponent = 3 - player
    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == player:
                directions_free = len(state.directions_available_from((i, j)))
                if directions_free == 0:
                    counter -= 100
                elif directions_free == 1:
                    counter -= 5
            
            elif state.board[i][j] == opponent:
                directions_free = len(state.directions_available_from((i, j)))
                if directions_free == 0:
                    counter += 100
                elif directions_free == 1:
                    counter += 5
    return counter

def heuristic_function5(state, player):
    opponent = 3 - player
    if state.winner == player:
        return math.inf // 2
    elif state.winner == opponent:
        return -math.inf // 2

    counter = 0
    for i in range(state.width):
        for j in range(state.width):
            if state.board[i][j] == player:
                if len(state.directions_available_from((i, j))) == 1:
                    counter -= 1
            elif state.board[i][j] == opponent:
                if len(state.directions_available_from((i, j))) == 1:
                    counter += 1
            
            
    return counter


def execute_random_move(game, key=None):
    
    # Start counting time
    start_time = time.time()
    (moveFrom, moveTo) = random.choice(game.state.available_moves())
    game.state = game.state.move(moveFrom, moveTo)

    # Print time
    print("Time: ", time.time() - start_time)

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
    


# MONTE CARLO MOVE ========================================================================================================

class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.value = 0
        self.visits = 0

    def ucb1(self):
        if self.visits == 0:
            return math.inf
        return self.value / self.visits + 2 * math.sqrt(math.log(self.parent.visits) / self.visits)
    

def execute_monte_carlo_move(iterations):

    def monte_carlo_move(game, key=None):

        root = Node(game.state)
        
        for i in range(iterations):
            leaf = traverse(root)
            winner = rollout(leaf)
            backpropagate(leaf, winner)
        
        # print_monte_carlo_tree(root, 0)

        best_child = max(root.children, key=lambda child: child.visits)
        game.state = best_child.state

    return monte_carlo_move



def traverse(node):
    # Traverse a tree until a leaf node is found (pick the best child node at each step)
    while len(node.children) > 0:
        max_value = max(node.children, key=lambda child: child.ucb1()).ucb1()
        node = random.choice([child for child in node.children if child.ucb1() == max_value])
    
    # If the leaf node has not been visited, return it
    if node.visits == 0 or node.state.winner != -1: 
        return node
    
    # If the leaf node has been visited, expand it and return a random child node
    else:
        node.children = [Node(node.state.move(move[0], move[1]), node) for move in node.state.available_moves()]
        return random.choice(node.children)


def rollout(node):
    # Rollout a random game from the given node
    state = node.state
    while state.winner == -1:
        (moveFrom, moveTo) = random.choice(state.available_moves())
        state = state.move(moveFrom, moveTo)
    
    return state.winner
    

def backpropagate(node, winner):
    # Backpropagate the winner of a rollout to all parent nodes
    while node is not None:
        node.visits += 1
        if node.state.player != winner:
            node.value += 1
        node = node.parent


def print_monte_carlo_tree(node, depth):
    if (depth > 1): return
    print("  " * depth, node.state.player, node.value, node.visits)
    for child in node.children:
        print_monte_carlo_tree(child, depth + 1)


