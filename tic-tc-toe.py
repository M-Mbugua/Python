import random
def display_board(board):

    print('    |     |')
    print(' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    # print('   |    |')
    print('---------------')
    print('    |     |')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    # print('   |    |')
    print('---------------')
    print('    |     |')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    # print('   |    |')


def player_input():
    choice = ''
    acceptable_values = ['X','O']

    while choice not in acceptable_values:
        choice = input("Do you want to be X or O? ").upper()

        if choice not in acceptable_values:
            print("Sorry, but you can only choose X or O. Please try again.")

    if choice == 'X':
        return 'X', 'O'

    if choice == 'O':
        return 'O', 'X'

def place_choice(board, choice, position):
    board[position] = choice


def who_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def win_check(board, mark):
    return board[7] == mark and board[8] == mark and board[9] == mark or \
        board[4] == mark and board[5] == mark and board[6] == mark or \
        board[1] == mark and board[2] == mark and board[3] == mark or \
        board[7] == mark and board[5] == mark and board[3] == mark or \
        board[1] == mark and board[5] == mark and board[9] == mark or \
        board[7] == mark and board[4] == mark and board[1] == mark or \
        board[8] == mark and board[5] == mark and board[2] == mark or \
        board[9] == mark and board[6] == mark and board[3] == mark


def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("Welcome to Tic Tac Toe")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = who_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)

            print("Player 1 play")

            position = player_choice(theBoard)
            place_choice(theBoard, player1_marker, position)


            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)

            print("Player 2 play")

            position = player_choice(theBoard)
            place_choice(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break









