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
TIE = "TIE"


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


def init_board(board):
    """Returns an empty 3-by-3 board (with .)."""
    print("\n\t", board[0], " | ", board[1], " | ", board[2],       "     1 |  2  | 3")
    print("\t", "---+-----+----   ----+-----+---")
    print("\t", board[3], " | ", board[4], " | ", board[5],         "     4 |  5  | 6")
    print("\t", "---+-----+----   ----+-----+---")
    print("\t", board[6], " | ", board[7], " | ", board[8],         "     7 |  8  | 9", "\n")
    return board


def get_move(board, player):

    print(player + "'s turn.")
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

    return position


def get_move_2(board, player2):

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

    return position


def get_move_computer(board, computer):

     print(computer + "'s turn.")
     position = random.randint(0,8)
     while board[position] != ".":
         position = random.randint(0,8)

     os.system("cls || clear")
     board[position] = computer
     init_board(board)
     return position


def get_move_computer_hard(board, computer_hard, player):

    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7) 
    BEST_MOVES2 = (4, 5, 7, 6, 8, 2, 3, 1, 0) 
    BEST_MOVES3 = (4, 6, 1, 0, 8, 2, 3, 5, 7) 
    print(computer_hard + "'s turn.")
    
    for position in legal_moves(board):
        board[position] = computer_hard
        if check_if_game_over(board) == computer_hard:
            print("Computer_hard choose", + position+1)  
            return position
        board[position] = EMPTY

    for position in legal_moves(board):
        board[position] = player
        if check_if_game_over(board) == player:
            print("Computer_hard choose", + position+1)  
            return position
        board[position] = EMPTY
    
    if board[0] != EMPTY and board[8] != EMPTY:
        for position in BEST_MOVES2:
             if position in legal_moves(board):
                print("Computer_hard choose", + position+1)  
                return position   

    elif board[5] != EMPTY and board[7] != EMPTY:
        for position in BEST_MOVES2:
             if position in legal_moves(board):
                print("Computer_hard choose", + position+1)  
                return position   
    
    elif board[2] != EMPTY and board[6] != EMPTY:
        for position in BEST_MOVES3:
             if position in legal_moves(board):
                print("Computer_hard choose", + position+1)  
                return position

    elif board[0] != EMPTY and board[7] != EMPTY:
        for position in BEST_MOVES3:
             if position in legal_moves(board):
                print("Computer_hard choose", + position+1)  
                return position   

    else:
        for position in BEST_MOVES:
             if position in legal_moves(board):
                print("Computer_hard choose", + position+1)  
                return position   
  

def legal_moves(board):
    
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def flip_player(turn):
  
    if turn == X:
       return O
    else:
        return X


def check_if_game_over(board):

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
            print("Winner is : ", winner)
            return winner

    if EMPTY not in board:
        print("Tie")
        return TIE

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
    os.system("cls || clear")
    init_board(board)
    player, player2 = first_move()
    turn = X
    while not check_if_game_over(board):

        if turn == player:
            
            position = get_move(board, player)
            board[position] = player
                 
        elif turn == player2:
            
            position = get_move_2(board, player2)
            board[position] = player2

        os.system("cls || clear")
        init_board(board)           
        turn = flip_player(turn) 


def tictactoe_game_comp():
    os.system("cls || clear")
    init_board(board)
    computer, player = first_move()
    turn = X

    while not check_if_game_over(board):

        if turn == player:
            
            position = get_move(board, player)
            board[position] = player
                      
        elif turn == computer:
            
            position = get_move_computer(board, computer)
            board[position] = computer

        os.system("cls || clear")
        init_board(board)           
        turn = flip_player(turn) 


def tictactoe_game_comp_hard():

    os.system("cls || clear")
    init_board(board)
    computer_hard, player = first_move()
    turn = X

    while not check_if_game_over(board) and game_still_going:

        if turn == player:
            
            position = get_move(board, player)
            board[position] = player
                 
        elif turn == computer_hard:
            
            position = get_move_computer_hard(board, computer_hard, player)
            board[position] = computer_hard

        os.system("cls || clear")
        init_board(board)           
        turn = flip_player(turn) 


def tictactoe_game_comp_hard_vs_comp():

    os.system("cls || clear")
    init_board(board)
    computer, computer_hard = first_move()
    turn = X
    
    while not check_if_game_over(board) and game_still_going:

        if turn == computer:
            
            position = get_move_computer(board, computer)
            board[position] = computer
                 
        elif turn == computer_hard:
            
            position = get_move_computer_hard(board, computer_hard, computer)
            board[position] = computer_hard

        os.system("cls || clear")
        init_board(board)           
        turn = flip_player(turn) 


def end_game():
    print("\n\n#########    END GAME    #########")
    print("\n\n")
    input("\n\nPress Enter")
    return None


def main_menu():
   
    choose_menu = menu()
    while choose_menu is None:
        choose_menu = menu()

    if choose_menu == 1:

        tictactoe_game()
        end_game()
           
    elif choose_menu == 2:

        comp_lv = level_input()
        while comp_lv is None:
            comp_lv = level_input()
        if comp_lv == 1:
            tictactoe_game_comp()
            end_game()
        elif comp_lv == 2:
            tictactoe_game_comp_hard()
            end_game()
        else:
            end_game()
        

    elif choose_menu == 3:
        tictactoe_game_comp_hard_vs_comp()
        end_game()
        

    elif choose_menu == 4:
        end_game()
        
if __name__ == '__main__':
    main_menu()
    