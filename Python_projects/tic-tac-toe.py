# this Game is not Complate ...

from random import randint

player, computer = "x", "o"
borde = list(range(1, 10))


def show_borde():
    for i in borde:
        end = " "
        if (j := 1) % 3 == 0:
            end = "\n"
        print(f'[{i}]', end=end)
        j += 1


def has_empty_space():
    return borde.count("x") + borde.count('o') != 9


def computer_move():
    while (c_move := 10) in borde:
        c_move = randint(1, 9)

    borde[c_move] = "o"


def chake_game(number):
    if borde[number] != 'x':
        borde[number] = "x"
        computer_move(number)
        show_borde()

    else:
        print('you choose this before!\nchose agene')


print("Player is : x\nComputer is : o\n")
show_borde()
while has_empty_space():
    match(move := int(input('Enter You Move : '))):
        case 1:
            chake_game(0)
        case 2:
            chake_game(1)
        case 3:
            chake_game(2)
        case 4:
            chake_game(3)
        case 5:
            chake_game(4)
        case 6:
            chake_game(5)
        case 7:
            chake_game(6)
        case 8:
            chake_game(7)
        case 9:
            chake_game(8)
        case _:
            print('you moset choose one of the borde number :')
            show_borde()
            continue
