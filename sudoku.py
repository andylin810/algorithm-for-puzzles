
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def findNext(puzzle):
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                return i, j
    return -1, -1


def isValid(puzzle, i, j, n):
    # check column
    for row in range(0, 9):
        if puzzle[row][j] == n:
            return False
    # check row
    for col in range(0, 9):
        if puzzle[i][col] == n:
            return False
    # check sections
    startRow = (i // 3) * 3
    startCol = j // 3 * 3
    for row in range(startRow, startRow+3):
        for col in range(startCol, startCol+3):
            if grid[row][col] == n:
                return False
    return True


def solveSudoku(puzzle):
    i, j = findNext(puzzle)
    # no more available box to be solved ( game is done)
    if (i, j) == (-1, -1):
        printPuzzle(puzzle)
        return True

    for number in range(1, 10):
        if isValid(puzzle, i, j, number):
            puzzle[i][j] = number
            if solveSudoku(puzzle):
                return True
            else:
                puzzle[i][j] = 0
    return False


def printPuzzle(puzzle):
    for row in puzzle:
        string = ""
        for num in row:
            string += str(num) + " "
        print(string)

solveSudoku(grid)