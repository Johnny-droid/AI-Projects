from copy import deepcopy

EMPTY = 0
OUTSIDE = -1

# 0 = empty space
# 1 = player 1
# 2 = player 2
# 3 = vertical connector
# 4 = horizontal connector
# 5 = down-right connector
# 6 = down-left connector
# 7 = up-right connector
# 8 = up-left connector


board0 = [
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1],
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1],
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1],
    [  1,  1,  1,  1,  0,  2,  2,  2,  2],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [  1,  1,  1,  1,  0,  2,  2,  2,  2],
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1],
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1],
    [ -1, -1, -1,  0,  0,  0, -1, -1, -1]
]

vboard0 = [
    [ 5,  4,  4,  0,  0,  0,  4,  4,  6],
    [ 3,  5,  4,  0,  0,  0,  4,  6,  3],
    [ 3,  3,  5,  0,  0,  0,  6,  3,  3],
    [ 1,  1,  1,  1,  0,  2,  2,  2,  2],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 1,  1,  1,  1,  0,  2,  2,  2,  2],
    [ 3,  3,  7,  0,  0,  0,  8,  3,  3],
    [ 3,  7,  4,  0,  0,  0,  4,  8,  3],
    [ 7,  4,  4,  0,  0,  0,  4,  4,  8]
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
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [ 1,  1,  1,  1, 0, 0, 0, 0,  2,  2,  2,  2],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [ 0,  0,  0,  0, 0, 0, 0, 0,  0,  0,  0,  0],
    [ 1,  1,  1,  1, 0, 0, 0, 0,  2,  2,  2,  2],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1]
]

vboard1 = [
    [ 5,  4,  4,  4,  0,  0,  0,  0,  4,  4,  4,  6],
    [ 3,  5,  4,  4,  0,  0,  0,  0,  4,  4,  6,  3],
    [ 3,  3,  5,  4,  0,  0,  0,  0,  4,  6,  3,  3],
    [ 3,  3,  3,  5,  0,  0,  0,  0,  6,  3,  3,  3],
    [ 1,  1,  1,  1,  0,  0,  0,  0,  2,  2,  2,  2],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 1,  1,  1,  1,  0,  0,  0,  0,  2,  2,  2,  2],
    [ 3,  3,  3,  7,  0,  0,  0,  0,  8,  3,  3,  3],
    [ 3,  3,  7,  4,  0,  0,  0,  0,  4,  8,  3,  3],
    [ 3,  7,  4,  4,  0,  0,  0,  0,  4,  4,  8,  3],
    [ 7,  4,  4,  4,  0,  0,  0,  0,  4,  4,  4,  8]
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
            self.vboard = vboard0
            self.connections = connections0
            self.width = 9
        elif board_number == 1:
            self.board = board1
            self.vboard = vboard1
            self.connections = connections1
            self.width = 12
        
        self.player = 1
        self.winner = -1

    def move(self, moveFrom, moveTo):

        new_state = deepcopy(self)
        new_state.board[moveTo[0]][moveTo[1]] = self.board[moveFrom[0]][moveFrom[1]]
        new_state.vboard[moveTo[0]][moveTo[1]] = self.vboard[moveFrom[0]][moveFrom[1]]
        new_state.board[moveFrom[0]][moveFrom[1]] = EMPTY
        new_state.vboard[moveFrom[0]][moveFrom[1]] = EMPTY
        new_state.player = 3 - self.player
        new_state.update_winner()

        return new_state
    
    # Checks if around the last move, the pieces still have available moves (performance improvement compared to the below version, but not that much)
    # There are some situations where it doesn't work, that's why I left the below version
    # def update_winner(self, last_move):
    #     pieces = self.nearby_pieces_from(last_move)

    #     for nearby_piece in pieces:
    #         if self.board[nearby_piece[0]][nearby_piece[1]] == EMPTY:
    #             continue

    #         if len(self.available_moves_from(nearby_piece)) == 0:
    #             self.winner = 3 - self.board[nearby_piece[0]][nearby_piece[1]]
    #             return self.winner
    #     return -1

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
    

    # Returns a list of moves from a given position
    def available_moves_from(self, pos):
        moves = set()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = pos[0], pos[1]
        done = False
        for i in range(len(directions)):
            d = directions[i]
            i, j = x, y
            while not done:
                prev_i, prev_j = i, j
                i = (i+d[0]) % self.width
                j = (j+d[1]) % self.width
                if self.board[i][j] == EMPTY:
                    moves.add(((x, y), (i, j)))
                elif self.board[i][j] == OUTSIDE and self.board[self.connections[prev_i][prev_j][0]][self.connections[prev_i][prev_j][1]] == EMPTY:
                    moves.add(((x, y), self.connections[prev_i][prev_j]))
                    i, j = self.connections[prev_i][prev_j][0], self.connections[prev_i][prev_j][1]
                    d[0] , d[1] = ((i-prev_i) // abs(i-prev_i) - d[0]), ((j-prev_j) // abs(j-prev_j)) - d[1]
                else:
                    done = True
            done = False

        return list(moves)
            
    

    # Returns a list of moves of 1 step from a given position (it's used to check in how many sides a piece is blocked)
    def directions_available_from(self, pos):
        moves = []
        i, j = pos[0], pos[1]

        # UP
        if self.board[(i-1)%self.width][j] == EMPTY:
            moves.append(((i, j), ((i-1)%self.width, j)))
        elif self.board[(i-1)%self.width][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))

        # DOWN
        if self.board[(i+1)%self.width][j] == EMPTY:
            moves.append(((i, j), ((i+1)%self.width, j)))
        elif self.board[(i+1)%self.width][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # LEFT
        if self.board[i][(j-1)%self.width] == EMPTY:
            moves.append(((i, j), (i, (j-1)%self.width)))
        elif self.board[i][(j-1)%self.width] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))
        
        # RIGHT
        if self.board[i][(j+1)%self.width] == EMPTY:
            moves.append(((i, j), (i, (j+1)%self.width)))
        elif self.board[i][(j+1)%self.width] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
            moves.append(((i, j), self.connections[i][j]))

        return moves


    # Used for updating the winner around a specific piece (used to improve performance)
    # def nearby_pieces_from(self, pos):
    #     pieces = []
    #     i, j = pos[0], pos[1]

    #     # UP
    #     if self.board[(i-1)%self.width][j] != EMPTY and self.board[(i-1)%self.width][j] != OUTSIDE:
    #         pieces.append(((i-1)%self.width, j))
    #     elif self.board[(i-1)%self.width][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
    #         pieces.append(self.connections[i][j])

    #     # DOWN
    #     if self.board[(i+1)%self.width][j] != EMPTY and self.board[(i+1)%self.width][j] != OUTSIDE:
    #         pieces.append(((i+1)%self.width, j))
    #     elif self.board[(i+1)%self.width][j] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
    #         pieces.append(self.connections[i][j])
        
    #     # LEFT
    #     if self.board[i][(j-1)%self.width] != EMPTY and self.board[i][(j-1)%self.width] != OUTSIDE:
    #         pieces.append((i, (j-1)%self.width))
    #     elif self.board[i][(j-1)%self.width] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
    #         pieces.append(self.connections[i][j])
        
    #     # RIGHT
    #     if self.board[i][(j+1)%self.width] != EMPTY and self.board[i][(j+1)%self.width] != OUTSIDE:
    #         pieces.append((i, (j+1)%self.width))
    #     elif self.board[i][(j+1)%self.width] == OUTSIDE and self.board[self.connections[i][j][0]][self.connections[i][j][1]] == EMPTY:
    #         pieces.append(self.connections[i][j])

    #     return pieces