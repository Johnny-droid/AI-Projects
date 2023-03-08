from copy import deepcopy

EMPTY = 0
OUTSIDE = -1

board0 = [
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

connections0 = [
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

board1 = [
    [-1, -1, -1, -1, 2, 0, 0, 2, -1, -1, -1, -1],
    [-1, -1, -1, -1, 2, 0, 0, 2, -1, -1, -1, -1],
    [-1, -1, -1, -1, 2, 0, 0, 2, -1, -1, -1, -1],
    [-1, -1, -1, -1, 2, 0, 0, 2, -1, -1, -1, -1],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [-1, -1, -1, -1, 1, 0, 0, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, 0, 0, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, 0, 0, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, 0, 0, 1, -1, -1, -1, -1]
]

connections1 = [
    [(0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (0, 0), (0, 0), (4,11), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (4, 1), (0, 0), (0, 0), (4,10), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (4, 2), (0, 0), (0, 0), (4, 9), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (4, 3), (0, 0), (0, 0), (4, 8), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 4), (1, 4), (2, 4), (3, 4), (0, 0), (0, 0), (0, 0), (0, 0), (3, 7), (2, 7), (1, 7), (0, 7)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(11,4), (10,4), (9, 4), (8, 4), (0, 0), (0, 0), (0, 0), (0, 0), (8, 7), (9, 7), (10,7), (11,7)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (7, 3), (0, 0), (0, 0), (7, 8), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (7, 2), (0, 0), (0, 0), (7, 9), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (7, 1), (0, 0), (0, 0), (7,10), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (7, 0), (0, 0), (0, 0), (7,11), (0, 0), (0, 0), (0, 0), (0, 0)]
]

class State:
    
    connections = []

    def __init__(self, board_number):

        if board_number == 0:
            self.board = board0
            self.connections = connections0
            self.width = 9
        elif board_number == 1:
            self.board = board1
            self.connections = connections1
            self.width = 12
        
        self.player = 1
        self.winner = -1

    def move(self, moveFrom, moveTo):

        new_state = deepcopy(self)
        new_state.board[moveTo[0]][moveTo[1]] = self.board[moveFrom[0]][moveFrom[1]]
        new_state.board[moveFrom[0]][moveFrom[1]] = EMPTY
        new_state.player = 3 - self.player
        
        self.update_winner()

        return new_state
    
    def update_winner(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] == 1 or self.board[i][j] == 2:
                    # If the piece is blocked, the opponent wins
                    if len(self.available_moves_from((i, j))) == 0:
                        self.winner = 3 - self.board[i][j]
                        return self.winner
        return -1


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
        if self.board[(i+1)%self.width][j] == EMPTY:
            moves.append(((i, j), ((i+1)%self.width, j)))
        elif self.board[(i+1)%self.width][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # LEFT
        if self.board[i][(j-1)] == EMPTY:
            moves.append(((i, j), (i, (j-1))))
        elif self.board[i][(j-1)] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # RIGHT
        if self.board[i][(j+1)%self.width] == EMPTY:
            moves.append(((i, j), (i, (j+1)%self.width)))
        elif self.board[i][(j+1)%self.width] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))

        return moves
