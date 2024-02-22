from random import randint

board = []
# creates a board of 5x5 
for x in range(0,5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print((" ").join(row))

def random_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board) - 1)
    return ship_row, ship_col


def guess_ship(board):
    guess_row = int(input("guess a row between 1-5: "))
    guess_col = int(input("gess a column between 1-5: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congrats you have sunk my battleship!")

    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("you must guess a number between 1-5")



