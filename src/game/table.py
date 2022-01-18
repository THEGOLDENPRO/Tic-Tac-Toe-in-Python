import numpy
from . import render

class board(): #The console board.
    def __init__(self, rows, cols, screen):
        # Creates board.
        self.board = numpy.zeros((rows, cols))
        
        self.rows = rows
        self.cols = cols
        self.screen = screen

        #Assign sub classes.
        self.square = self.square_(self.board)

    class square_: #Sub class for squares.
        def __init__(self, board):
            self.board = board
            pass

        def mark(self, row, col, player:int): #Places either "O" or "X" in specified square on board.
            self.board[row][col] = player

        def is_available(self, row, col): #Checks if square is available.
            if self.board[row][col] == 0:
                return True
            else:
                return False

    def get(self): #Returns actual board.
        return self.board

    def is_full(self): #Returns True or False if whole board is full.
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return False
        return True

    def check_win(self, player:int):
        # Check vertical win.
        for col in range(self.cols):
            
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                render.draw_vertical_winning_line(self.screen, col, player)
                return True

        # Check horizontal win
        for row in range(self.rows):
            
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                render.draw_horizontal_winning_line(self.screen, row, player)
                return True

        # Check asc diagonal win
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            render.draw_asc_diagonal(self.screen, player)
            return True

        # Check desc diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            render.draw_desc_diagonal(self.screen, player)
            return True

        return False

    def print(self):
        print(self.board)