# create a list of squares
SPACES = list('123456789')

# initialilze an empty dictionary
game_board = {}
for space in SPACES:
    game_board[space] = ' '


def print_board(b):
    Print(f'''
    {b['1']} | {b['2']} | {b['3']} 1 2 3
    --+---+--
    {b['4']} | {b['5']} | {b['6']} 4 5 6
    --+---+--
    {b['7']} | {b['8']} | {b['9']} 7 8 9
  ''')

    print_board(game_board)
