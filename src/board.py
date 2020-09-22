import numpy as np
from collections import defaultdict

class QueenBoard:
    def __init__(self, createNew, board):
        self.confilcts = 0
        self.conflictDict = defaultdict(int)
        if createNew:
            self.createBoard()
            self.fitness = self.getFitness(self.board)
        else:
            self.board = board
            self.fitness = self.getFitness(self.board)
        #print(self.board)
        #print(self.fitness)

    def getNeigbors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board.T)):
                cell = self.board[row][col]
                if cell != 1:
                    continue

    def createBoard(self):
        board = np.zeros((25, 25), dtype='int')
        for i in range(25):
            board[i][0] = 1
        self.board = board

    def getFitness(self, board):
        fitness = 0
        for row in range(len(board)):
            for col in range(len(board.T)):
                cell = self.board[row][col]
                if cell != 1:
                    continue
                fitness -= self.numOfConflicts(row, col, board)

        return fitness


    def numOfConflicts(self, row, col, board):
        curCon = 0
        curCon += self.checkUp(row, col, board)
        curCon += self.checkDown(row, col, board)
        curCon += self.checkUpLeft(row, col, board)
        curCon += self.checkUpRight(row, col, board)
        curCon += self.checkDownLeft(row, col, board)
        curCon += self.checkDownRight(row, col, board)

        return curCon

    def checkUp(self, row, col, board):
        ogRow = row
        while row > 0:
            row -= 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0

    def checkDown(self, row, col, board):
        ogRow = row
        while row < (len(board) - 1):
            row += 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0

    def checkUpLeft(self, row, col, board):
        ogRow = row
        while row > 0 and col > 0:
            row -= 1
            col -= 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0

    def checkUpRight(self, row, col, board):
        ogRow = row
        while row > 0 and col < (len(board) - 1):
            row -= 1
            col += 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0

    def checkDownLeft(self, row, col, board):
        ogRow = row
        while row < (len(board) - 1) and col > 0:
            row += 1
            col -= 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0

    def checkDownRight(self, row, col, board):
        ogRow = row
        while row < (len(board) - 1) and col < (len(board) - 1):
            row += 1
            col += 1
            curCell = board[row][col]
            if curCell == 1:
                self.conflictDict[ogRow] += 1
                return 1
        return 0
