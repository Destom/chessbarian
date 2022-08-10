import math
import random

class Board():
    def __init__(self,size):
        tmp_board = []
        self.size = size
        board_range = range(0,size)
        board_row = list(map(lambda board_square: '*' , board_range ))
        board_main = list(map(lambda board: list(board_row),board_range))
        self.board=board_main
        #print(self.board)
    
    def print_board(self):
        #print('this is the map attempt')
        #print(list(map(lambda item: print(item), self.board)))
        #print('this is the for loop attempt')
        for item in self.board:
            print (item)
    
    def put_piece(self,piece):
        self.board[piece.location[0]][piece.location[1]] = 'B'
    
class Piece:
    def __init__(self):
        self.move_lists = {'king':[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]}
    
    def available_moves(self,board):
        possible_moves = []
        for move in self.moves:
            move_location = [self.location[0] + move[0],self.location[1] + move[1]]
            if move_location[0] >= 0 and move_location[0] <= board.size -1:
                if move_location[1] >= 0 and move_location[1] <= board.size -1:
                    possible_moves.append(move_location)
        possible_moves.reverse()
        return possible_moves

class ceture(Piece):
    def __init__(self,board,id):
        super().__init__()
        available_spaces = []
        row_num = -1
        cell_num = -1
        for row in board.board:
            row_num += 1
            for cell in row:
                cell_num += 1
                if cell == '*':
                    available_spaces.append([row_num,cell_num])
            cell_num = -1
        space = random.choice(available_spaces)
        self.id = id
        board.board[space[0]][space[1]] = 'C'

class Barian(Piece):
    def __init__(self,board):
        self.location = [board.size -1 ,math.ceil(board.size/2) -1]
        self.alive = True
        super().__init__()
        self.moves = self.move_lists['king']
    
    def barian_move(self,board):
        counter = 0
        move_choice = 0
        move_list = {}
        tmp_board = Board(board.size)
        for move in self.available_moves(board):
            counter+=1
            move_list[counter] = move
            tmp_board.board[move[0]][move[1]] = str(counter)
        while move_choice not in (move_list.keys()):
            tmp_board.board[self.location[0]][self.location[1]] = 'B'
            print('''
The barians available moves are''')
            tmp_board.print_board()
            move_choice = int(input('what move would you like to make?: '))
        print (f'you chose move {move_list[move_choice]}')
        board.board[self.location[0]][self.location[1]] = '*'
        new_location = move_list[move_choice] 
        self.location = new_location
        board.board[self.location[0]][self.location[1]] = 'B'