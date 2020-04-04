import pygame
from main import backtracking, isvalid
import time
pygame.font.init()


class Screen:
    game = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.model = None
        self.cube = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.selected = None

    def update(self):
        self.model = [[self.cube[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cube[row][col].value == 0:
            self.cube[row][col].set(val)
            self.update()

            if isvalid(self.model, val, (row, col)) and backtracking(self.model):
                return True
            else:
                self.cube[row][col].set(0)
                self.cube[row][col].set_temp(0)
                self.update()
                return False

    def sketch(self, value):
        row, col = self.selected
        self.cube[row][col].set_temp(value)


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def set(self, value):
        self.value = value

    def set_temp(self, value):
        self.temp = value
