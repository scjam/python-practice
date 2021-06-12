# create a list of squares
SPACES = list('123456789')

# initialilze an empty dictionary
game_board = {}
for space in SPACES:
    game_board[space] = ' '
active = True
current_player = 'X'
next_player = 'O'


def print_board(b):
    print(f'''
    {b['1']} | {b['2']} | {b['3']} 1 2 3
    --+---+--
    {b['4']} | {b['5']} | {b['6']} 4 5 6
    --+---+--
    {b['7']} | {b['8']} | {b['9']} 7 8 9
  ''')


def is_winner(b, player):
    return ((b['1'] == b['2'] == b['3'] == player) or  # Across the top
            (b['4'] == b['5'] == b['6'] == player) or  # Across the middle
            (b['7'] == b['8'] == b['9'] == player) or  # Across the bottom
            (b['1'] == b['4'] == b['7'] == player) or  # Down the left
            (b['2'] == b['5'] == b['8'] == player) or  # Down the middle
            (b['3'] == b['6'] == b['9'] == player) or  # Down the right
            (b['3'] == b['5'] == b['7'] == player) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == player))   # Diagonal

# print_board(game_board)
# game_board[b['1']] = 'X'
# game_board[b['9']] = 'O'
# print_board(game_board)


while active:
    print_board(game_board)
    print(f"Your move {current_player}!")
    valid_move = False
    while not valid_move:
        space = input("Please enter a space: 1-9\n")
        print(f"You entered: {space}")
        # if(space == 'q'):
        #     valid_move = False
        #     active = False
        if space in SPACES and game_board[space] == ' ':
            valid_move = True
            game_board[space] = current_player

    if is_winner(game_board, current_player):
        print(f"You have won {current_player}! Way to go!")
        print_board(game_board)
        active = False

    elif not ' ' in game_board.values():
        print("Cats game!")
        print_board(game_board)
        active = False

    else:
        current_player, next_player = next_player, current_player
