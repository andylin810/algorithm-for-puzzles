import numpy as np


matrix = np.zeros((8, 8))

horizontal = np.zeros(8)
vertical = np.zeros(8)
numQueen = 0


def checkDiagnal(board, x, y):
    occupied = False
    length = min(x, y)
    i = x - length
    j = y - length

    while(i < 8 and j < 8):
        if board[i][j] != 0:
            occupied = True
            return occupied
        else:
            i += 1
            j += 1

    length = min(x, 7-y)
    i = x - length
    j = y + length

    while(j >= 0 and i < 8):
        if board[i][j] != 0:
            occupied = True
            return occupied
        else:
            i += 1
            j -= 1
    return occupied


def nextToFill(board):
    global numQueen
    n = -1
    if numQueen == 8:
        return n
    for i in range(0,8):
        if horizontal[i] == 0:
            return i
    return -2


def checkValid(board,x,y):
    if horizontal[x] == 0 and vertical[y]==0 and not checkDiagnal(board,x,y):
        return True
    else:
        return False

def fillQueen(board,x,y):
    global numQueen
    board[x][y] = 1
    horizontal[x] = 1
    vertical[y] = 1
    numQueen += 1


def solveQueen(board):
    global numQueen
    n = nextToFill(board)
    if n == -1:
        print(matrix)
        return True
    if n == -2:
        return False
    else:
        for number in range(0, 8):
            if checkValid(board,n,number):
                fillQueen(board,n,number)
                if solveQueen(board):
                    return True
                else:
                    board[n][number] = 0
                    horizontal[n] = 0
                    vertical[number] = 0
                    numQueen -= 1
solveQueen(matrix)
    