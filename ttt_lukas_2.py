###################################
#########   TicTacToe   ###########
###################################
import random
import os
os.system("cls || clear")


board = [".", ".", ".",
         ".", ".", ".",
         ".", ".", "."]

game_still_going = True
winner = None
EMPTY = "."
X = "X"
O = "O"
NUM_SQUARES = 9



def menu():


    print("-------------------------------------\n")
    print("-----------TicTacToe Game------------ \n")
    print("           CHOOSE OPTION     \n")
    print("PLAY PLAYER ON PLAYER     ---PRESS-----1")
    print("PLAY PLAYER ON COMPUTER   ---PRESS-----2")
    print("PLAY COMPUTER ON COMPUTER ---PRESS-----3")
    print("EXIT GAME                 ---PRESS-----4")
    input1= input("CHOOSE :   ")

    try:
        main_choose = int(input1)
        return main_choose
    except ValueError:
        return
    

def level_input():

    print("\n")
    print(" EASY GAME ---- PRESS ---- 1 ")
    print(" HARD GAME ---- PRESS ---- 2 ")
    print(" EXIT GAME ---- PRESS ---- 3 ")
    print("\n")
    input2 = input(" CHOOSE OPTION :   ")

    try:
        Ai_lv = int(input2)
        return Ai_lv
    except ValueError:
        return


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    print("\n\t", board[0], " | ", board[1], " | ", board[2],       "     1 |  2  | 3")
    print("\t", "---+-----+----   ----+-----+---")
    print("\t", board[3], " | ", board[4], " | ", board[5],         "     4 |  5  | 6")
    print("\t", "---+-----+----   ----+-----+---")
    print("\t", board[6], " | ", board[7], " | ", board[8],         "     7 |  8  | 9", "\n")
    return board


def get_move(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:

         while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
             position = input("Choose a position from 1-9: ")
         position = int(position) - 1 # dzięki temu pozycje 1-9 nie 0-8

         if board[position] == ".":
             valid = True
         else:
             print("You can't go there. Go again.")

    os.system("cls || clear")
    board[position] = player
    init_board()

def get_move_2(player2):

    print(player2 + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:

         while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
             position = input("Choose a position from 1-9: ")
         position = int(position) - 1

         if board[position] == ".":
             valid = True
         else:
             print("You can't go there. Go again.")

    os.system("cls || clear")
    board[position] = player2
    init_board()


def get_move_computer(computer):

     print(computer + "'s turn.")
     position = random.randint(0,8)
     while board[position] != ".":
         position = random.randint(0,8)

     os.system("cls || clear")
     board[position] = computer
     init_board()


def get_move_computer_hard(board, computer, player):

    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7) 
    print(computer + "'s turn.")
    print("Computer_hard choose", end=" ")
    for position in legal_moves(board):
        board[position] = computer
        if check_if_game_over(board) == computer:
            print(position)
            return position
        board[position] = EMPTY

    for position in legal_moves(board):
        board[position] = player
        if check_if_game_over(board) == player:
            print(position)
            return position
        board[position] = EMPTY

    for position in BEST_MOVES:
         if position in legal_moves(board):
            print(position)
            return position
  


def legal_moves(board):
    
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def flip_player(turn):
  
    if turn == X:
       return O
    else:
        return X

def check_if_game_over(board):

    global game_still_going   
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            game_still_going = False
            winner == "X" or winner == "O"
            print(str(winner) + " won.")

    if EMPTY not in board and winner != "X" and winner != "O" :
        game_still_going = False
        print("Tie")
        return 

    return None


def first_move():

    go_first = input("Are you first (t/n): ")
    if go_first == "t":
        print("\nYou have X")
        player = X
        computer = O
    else:
        print("\nYou have O")
        computer = X
        player = O
    return computer, player


def tictactoe_game():
    
    init_board()
    player, player2 = first_move()
    turn = X
    while game_still_going:

        if turn == player:
            
            get_move(player)
            check_if_game_over(board)
               
        elif turn == player2:
            
            get_move_2(player2)
            check_if_game_over(board)
                
        turn = flip_player(turn) 

    


def tictactoe_game_comp():
    
    init_board()
    computer, player = first_move()
    turn = X

    while game_still_going:

        if turn == player:
            
            get_move(player)
            check_if_game_over(board)
                      
        elif turn == computer:
            
            get_move_computer(computer)
            check_if_game_over(board)
                
        turn = flip_player(turn) 

    


def tictactoe_game_comp_hard():
    
    init_board()
    computer, player = first_move()
    turn = X

    while game_still_going:

        if turn == player:
            
            get_move(player)
            check_if_game_over(board)
                 
        elif turn == computer:
            
            get_move_computer_hard(board, computer, player)
            check_if_game_over(board)
                
        turn = flip_player(turn) 


    
def main_menu():
   
    choose_menu = menu()
    while choose_menu is None:
        choose_menu = menu()

    if choose_menu == 1:

        tictactoe_game()
        print("\n\n#########    END GAME    #########")
        print("\n\n")
           
    elif choose_menu == 2:

        comp_lv = level_input()
        while comp_lv is None:
            comp_lv = level_input()
        if comp_lv == 1:
            tictactoe_game_comp()
            print("\n\n#########    END GAME    #########")
            print("\n\n")
        elif comp_lv == 2:
            tictactoe_game_comp_hard()
            print("\n\n#########    END GAME    #########")
            print("\n\n")
        else:
            print("\n\n#########    END GAME    #########")
            print("\n\n")
        

    elif choose_menu == 3:
        print("\n\n#########    END GAME    #########")
        print("\n\n")
        

    elif choose_menu == 4:
        print("\n\n#########    END GAME    #########")
        print("\n\n")
        




if __name__ == '__main__':
    main_menu()