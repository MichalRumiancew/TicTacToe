import random
import os
import turtle

os.system("cls || clear")


#testowanie czy tablica drukije się poprawnie

def init_board():
    """Returns an empty 3-by-3 board (with .)."""

    # board = [".", ".", ".",
    #      ".", ".", ".",
    #      ".", ".", "."]

    board = [['.','.','.'],['.','.','.'],['.','.','.']]

# print(board)

#wybór jak ma wyglądać tablica do gry? 
# tablica 
# - | - | -     1 | 2 | 3
# - | - | -     4 | 5 | 6
# - | - | -     7 | 8 | 9
# lub 
#    A | B | C
#  1 - | - | -     
#  2 - | - | -     
#  3 - | - | -    

    print("\n")
    print("  1" + "   " + "2" + "   " + "3")
    print("A " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("B " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("C " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")
        
print(init_board)


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
    
