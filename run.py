from random import randint

board = []
# creates a board of 5x5 
for x in range(0,5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print((" ").join(row))


def battle_ships(board):
    for ship in range(3):
        ship_row, ship_col = randint(0,5), randint(0,5)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0,5), randint(0,5)
        board[ship_row][ship_col] = "X"


def find_ships():
    row = input("Guess a row between 1-5: ")
    col = input("guess a column between 1-5: ")
    while row or col not in "12345":
        print("you must guess a number between 1-5")
        row = input("Guess a row between 1-5: ")
        col = input("guess a column between 1-5: ")
    
    return int(row), int(col)

