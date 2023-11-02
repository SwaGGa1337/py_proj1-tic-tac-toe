board = {" ": " ", 'zero': 0, '1111': 1, '2222': 2,
         'ooo': 0, '00': "-", '01': "-", '02': "-",
         'one': 1, '10': "-", '11': "-", '12': "-",
         'two': 2, '20': "-", '21': "-", '22': "-"}

valid_xy = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
valid_char = ['x', 'o']

def print_field():
    count = 1
    for key, value in board.items():
        print(value, end=" ")
        count += 1
        if count > 4:
            count = 1
            print()

def win_game():
    if (board['00'] == board['01'] == board['02']) and (board['00'] in valid_char):
        return True
    elif (board['10'] == board['11'] == board['12']) and (board['10'] in valid_char):
        return True
    elif (board['20'] == board['21'] == board['22']) and (board['20'] in valid_char):
        return True
    elif (board['00'] == board['10'] == board['20']) and (board['00'] in valid_char):
        return True
    elif (board['01'] == board['11'] == board['21']) and (board['01'] in valid_char):
        return True
    elif (board['02'] == board['12'] == board['22']) and (board['02'] in valid_char):
        return True
    elif (board['00'] == board['11'] == board['22']) and (board['00'] in valid_char):
        return True
    elif (board['02'] == board['11'] == board['20']) and (board['02'] in valid_char):
        return True

    return False


def play():
    current_player = 1
    count_moves = 0
    player = 0
    while not win_game() and count_moves < 9:
        if current_player == 1:
            player = player1
        else:
            player = player2
        print_field()
        xy = str(input('Игрок {0}, введите координаты: '.format(player)))
        if xy in valid_xy:
            if board[xy] not in valid_char:
                if player == player1:
                    board[xy] = 'x'
                    current_player = 2 if current_player == 1 else 1
                elif player == player2:
                    board[xy] = 'o'
                    current_player = 2 if current_player == 1 else 1
                count_moves += 1
            else:
                print('-----------------------\n'
                      '-Это место уже занято!-\n'
                      '-----------------------')
        else:
            print('Неверное значение!')
    print_field()
    if win_game():
        print('----------------\nИгра закончена!')
        print('Игрок {0} победил!\n----------------'.format(player))
    else:
        print('Ничья!')

player1 = str(input('Первый игрок введите имя: '))
player2 = str(input('Второй игрок введите имя: '))
play()