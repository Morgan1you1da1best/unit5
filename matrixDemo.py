#Morgan Baughman
#11/17/17
#matrixDemo.py

board = [[‘a’,’b’,’c’],[‘d’,’e’,’f’],[‘g’,’h’,’i]]


def printBoard()
for row in range(0,3):
    for col in range(0,3):
        print(board[row][col],’ ‘,end= ‘’)
    print()
    
printBoard()

row =int(input(‘Enter a row number’))
col = int(input(‘Enter a col number’))

