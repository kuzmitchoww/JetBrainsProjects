# write your code here
line = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
shot = 'X'


def fill_cells(data, symbol):
    row = data[0] - 1
    col = data[1] - 1
    line[row][col] = symbol
    return line


def get_user_coordinates():
    global shot
    # ask for coordinates
    coordinates = input('Enter the coordinates:').split(sep=' ')
    # check if input is 2 symbols
    if len(coordinates) == 2:
        # check if input is integers
        if coordinates[0].isdigit() and coordinates[1].isdigit():
            coordinates = [int(i) for i in coordinates]
            # check if coordinates are in range
            if coordinates[0] in (1, 2, 3) and coordinates[1] in (1, 2, 3):
                global line
                row = coordinates[0] - 1
                col = coordinates[1] - 1
                if line[row][col] == ' ':
                    line = fill_cells(coordinates, shot)
                    if shot == 'X':
                        shot = 'O'
                    else:
                        shot = 'X'
                    field(line)
                    return True
                else:
                    print('This cell is occupied! Choose another one!')
                    return False

            else:
                print('Coordinates should be from 1 to 3!')
                return False
        else:
            print('You should enter numbers!')
            return False
    else:
        print('You should enter 2 numbers!')
        return False


def is_finished(data):
    if sum(i.count(' ') for i in data) != 0:
        return False
    else:
        return True


def row_col_diag(data):
    columns = [[i[x] for i in data] for x in range(3)]
    diagonals = [[data[0][0], data[1][1], data[2][2]], [data[0][2], data[1][1], data[2][0]]]
    for i in columns:
        if i.count(i[0]) == 3 and i[0] != ' ':
            return i[0]
    for i in diagonals:
        if i.count(i[0]) == 3 and i[0] != ' ':
            return i[0]
    for i in data:
        if i.count(i[0]) == 3 and i[0] != ' ':
            return i[0]


def field(data):
    print('---------')
    for i in data:
        print('|', *i, '|')
    print('---------')


def main(data):
    run = True
    field(line)
    while run:
        if not is_finished(line) and not row_col_diag(line):
            get_user_coordinates()
        else:
            if is_finished(line) and not row_col_diag(line):
                print('Draw')
            else:
                print(f'{row_col_diag(line)} wins')
            run = False


if __name__ == '__main__':
    main(line)
