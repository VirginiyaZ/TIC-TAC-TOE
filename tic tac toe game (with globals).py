game_board =['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']


show_time = True

winner = None

now_playing = 'X'

score_x = 0
score_o = 0

def play_game():
    global score_x 
    global score_o 
    display_board()
    
    
    while show_time:
        handle_turn(now_playing)
        game_over()
        next_player()
        
  
    if winner == 'X':
        score_x +=1
        print(winner + ' Победитель!')
    elif winner == 'O':
        score_o +=1
        print(winner + ' Победитель!')

    elif winner == None:
        print('Ничья!')
    
    
 
def display_board():

    print('\n')
    print(game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2] + '     1 | 2 | 3')
    print(game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5] + '     4 | 5 | 6')
    print(game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8] + '     7 | 8 | 9')
    print('\n')
    
def handle_turn(player):
    print(player + ' ходит')
    step = input('Выберите номер ячейки хода 1-9: ')

    valid = False       # в случае если ячейка уже занята (корректность хода)
    while not valid:

        while step not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            step = input('Выберите номер ячейки хода 1-9: ')

        step = int(step) - 1
        if game_board[step] == '-':
            valid = True
        else:
            print('Ячейка уже занята. Выберите другую.')    
    game_board[step] = player
    display_board()

def game_over():
    check_for_winner()
    check_for_draw()
    

def check_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
  
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    

def check_rows():
    global show_time
    row1 = game_board[0] == game_board[1] == game_board[2] != '-'
    row2 = game_board[3] == game_board[4] == game_board[5] != '-'
    row3 = game_board[6] == game_board[7] == game_board[8] != '-'
    if row1 or row2 or row3:
        show_time = False
    if row1:
        return game_board[0] 
    elif row2:
        return game_board[3] 
    elif row3:
        return game_board[6] 
    else:
        return None

def check_columns():
    global show_time
    column1 = game_board[0] == game_board[1] == game_board[2] != '-'
    column2 = game_board[3] == game_board[4] == game_board[5] != '-'
    column3 = game_board[6] == game_board[7] == game_board[8] != '-'
    if column1 or column2 or column3:
        show_time = False
    if column1:
        return game_board[0] 
    elif column2:
        return game_board[3] 
    elif column3:
        return game_board[6] 
    else:
        return None

def check_diagonals():
    global show_time
    diagonal1 = game_board[0] == game_board[4] == game_board[8] != '-'
    diagonal2 = game_board[2] == game_board[4] == game_board[6] != '-'
    if diagonal1 or diagonal2:
        show_time = False
    if diagonal1:
        return game_board[0] 
    elif diagonal2:
        return game_board[2]
    else:
        return None


def check_for_draw():
    global show_time
    if '-' not in game_board:
        show_time = False
        return True
    else:
        return False 
    
def next_player():
    global now_playing
    if now_playing == 'X':
        now_playing = 'O'
    elif now_playing == 'O':
        now_playing = 'X'
    

while True:
  play_game()
  
  print('Игрок O победил ' + str(score_o) + ' счет')
  print('Игрок X победил ' + str(score_x) + ' счет')
  
 
  if input('Сыграем? (да/нет): ') == 'нет':
    break

  
  game_board = ['-', '-', '-',
           '-', '-', '-',
           '-', '-', '-']
 
  
  show_time = True
  winner = None
  now_playing = 'X'

  
  if input('Обнулить счет (да/нет): ') == 'да':
    score_x = 0
    score_y = 0
    