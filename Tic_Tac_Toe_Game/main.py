# This is Tic Tac Toe Game
import os
import random
from os import system, name


# def clear_output():
#     print('\n'*10)

def clear_output():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def display_board(board):
    clear_output()
    print(f"  {board[7]} | {board[8]} | {board[9]} ")
    print(f"- - - - - - -")
    print(f"  {board[4]} | {board[5]} | {board[6]} ")
    print(f"- - - - - - -")
    print(f"  {board[1]} | {board[2]} | {board[3]} ")


# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
test_board = [' ']*10


def player_input():
    """
    OUTPUT = (Player1 marker, Player2 marker)
    :return:
    """
    player_marker = ""
    while player_marker not in ['O', 'X']:
        player_marker = input(f"Player 1: Do you want to be X or O? ").upper()
    if player_marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# print(player_input())
# test player_input function


def place_marker(board, marker, position):
    board[position] = marker


# clear_output()
# place_marker(test_board, 'O', 1)
# display_board(test_board)


def win_check(board, mark):
    # all rows, has same marker
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))
    # else:
    #     return False


# display_board(test_board)
# print(win_check(test_board, 'X'))


def choose_first():
    result_rand = random.randint(1, 2)
    if result_rand == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# print(choose_first())


def space_check(board, position):
    return board[position] == ' '


# display_board(test_board)
# print(space_check(test_board, 8))


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# display_board(test_board)
# print(full_board_check(test_board))


def player_choice(board):
    player_input_value = ""
    while player_input_value not in range(1, 10) or board[player_input_value] == 'X' or board[player_input_value] == 'O':
        player_input_value = int(input("Choose a position(1-9): "))
    if space_check(board, player_input_value):
        return player_input_value
    else:
        return False


# print(player_choice(test_board)


def reply():
    replay_again = ""
    while replay_again not in ['YES', 'NO', 'Y', 'N']:
        replay_again = input("\nDo you want to play again (Yes, No): ").upper()
    if replay_again == "YES" or replay_again == "Y":
        return True
    else:
        return False


print('|- - - - - - - - - - - - - - - - - - - |\n|  🎮 Welcome To Tic Tac Toe Game! 🎮  |\n|- - - - - - - - - - - - - - - - - - - |\n')
while True:
    test_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('\nReady to play? Y or N: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # player1 turn
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)

            if win_check(test_board, player1_marker):
                display_board(test_board)
                print("\n Player 1 has Won! 🥳🏆🥳\n")
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('\n Tie Game! 🤷\n')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # player2 turn
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)

            if win_check(test_board, player2_marker):
                display_board(test_board)
                print("\n Player 2 has Won! 🥳🏆🥳\n")
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('\n Tie Game! 🤷‍\n')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not reply():
        break
