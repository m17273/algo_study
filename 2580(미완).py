import sys

sudoku =  []
x = []
y = []
square = []

for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):

        if sudoku[i][j] == 0:

            for k in range(9):
                y.append(sudoku[k][j])
            for l in range(3):

            for num in range(9):
                if num not in sudoku[i] and num not in y and 



def solve():

    if len(s) == 9:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print()
