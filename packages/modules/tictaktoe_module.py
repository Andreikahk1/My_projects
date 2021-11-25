import random
import os

def new_board():
    # create an empty game field
    board = []
    for i in range(9):
        board.append(" ")
    return board

def display_board(board):
    # print a game field 
    board = board[:]
    for i in range(0,9):
        if board[i] not in ('X','O'):
            board[i] = i+1
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8],"\n")

def possible_move(board):
    # checking if selected move is possible
    move = []
    for i in range(9):
        if board[i] == " ":
            move.append(i)
    return move

def check_winner(board):
    # checking for winner
    win_list = ((0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
    for i in win_list:
        if (board[i[0]] == board[i[1]]) and (board[i[1]] == board[i[2]]) and (board[i[0]] != " "):
            return board[i[0]]
    if " " not in board:
        return "Draw"
    return None

def player_move(board, player):
    # player's move
    pos_move = possible_move(board)
    move = -1
    while move-1 not in pos_move:
        try:
            move = int(input("Please make a move (1 - 9): "))
            if move-1 not in pos_move:
                print("\nThis move is not possible, please choose another move (1 - 9):\n")   
        except ValueError:
            print("\nThis move is not possible, please choose another move (1 - 9):\n")   
    return move-1

def computer_move(board, computer, player):
    # computer's move -> just random move
    pos_move = possible_move(board)
    move = None
    while move not in pos_move:
        move = random.randint(0,8)
    return move

def tictaktoe():
    # clear the console
    clear = lambda: os.system('cls')
    clear()    
    # computer always plays as X and player as O
    computer, player = 'X', 'O'
    # X always moves first
    move = 'X'
    # starting new game
    board = new_board()
    # showing the game board
    display_board(board)
    # computer and player do moves until someone wins or Draw
    while not check_winner(board):
        if move == player:
            i = player_move(board, player)
            board[i] = player
        else:
            i = computer_move(board, computer, player)
            board[i] = computer
        display_board(board)
        if move == 'X':
            move = 'O'
        else:
            move = 'X'

    the_winner = check_winner(board)

    if the_winner != "Draw":
        if the_winner == computer:
            print("Computer wins!\n")
        else:
            print("Player wins!\n")
    else:
        print("It's a Draw!\n")
