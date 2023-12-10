board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
SX=0
SY=0
def score():
    print(f"Scores: X-{SX}|O-{SY}")
def print_board():
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
print_board()

def player_X():
    while True:
        row = int(input('enter the row number Player-X: '))
        column = int(input('enter the column number Player-X: '))
        if board[row - 1][column - 1] == '-':
            board[row - 1][column - 1] = 'X'
            break
        else:
            print('Cell already Selected..Choose a different one')
def player_O():
    while True:
        row = int(input('enter the row number Player-O: '))
        column = int(input('enter the column number Player-O: '))
        if board[row - 1][column - 1] == '-':
            board[row - 1][column - 1] = 'O'
            break
        else:
            print('Cell already Selected..Choose a different one')


game_on=True
count=9
while game_on:
    player_X()
    count-=1
    if count==0:
        print_board()
        print('GAME OVER')
        break
    elif ((board[0][0]== 'X'and board[1][0]== 'X' and board[2][0] == 'X') or (board[0][0]== 'X'and board[1][1]== 'X' and board[2][2] == 'X') or (board[0][0]== 'X'and board[0][1]== 'X' and board[0][2] == 'X')
        or (board[0][0]== 'X'and board[0][1]== 'X' and board[0][2] == 'X') or (board[0][1]== 'X'and board[1][1]== 'X' and board[2][1] == 'X')
        or (board[0][2]== 'X'and board[1][2]== 'X' and board[2][2] == 'X') or (board[1][0]== 'X'and board[1][1]== 'X' and board[1][2] == 'X')
        or (board[2][0]== 'X'and board[2][1]== 'X' and board[2][2] == 'X') or (board[2][0]== 'X'and board[1][1]== 'X' and board[0][2] == 'X')):
        print_board()
        print("X wins")
        break
    print_board()
    player_O()
    count-=1
    if count==0:
        print_board()
        print('GAME OVER')
        break
    elif ((board[0][0]== 'O'and board[1][0]== 'O' and board[2][0] == 'O') or (board[0][0]== 'O'and board[1][1]== 'O' and board[2][2] == 'O') or
          (board[0][0]== 'O'and board[0][1]== 'O' and board[0][2] == 'O')
        or (board[0][0]== 'O'and board[0][1]== 'O' and board[0][2] == 'O') or (board[0][1]== 'O'and board[1][1]== 'O' and board[2][1] == 'O')
        or (board[0][2]== 'O'and board[1][2]== 'O' and board[2][2] == 'O') or (board[1][0]== 'O'and board[1][1]== 'O' and board[1][2] == 'O')
        or (board[2][0]== 'O'and board[2][1]== 'O' and board[2][2] == 'O') or (board[2][0]== 'O'and board[1][1]== 'O' and board[0][2] == 'O')):
        print_board()
        print("O wins")
        break
    print_board()




