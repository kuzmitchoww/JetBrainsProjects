import random
import json

# create dominoes deck and game snake
dominoes = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
    [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
    [3, 3], [3, 4], [3, 5], [3, 6],
    [4, 4], [4, 5], [4, 6],
    [5, 5], [5, 6],
    [6, 6]
]
moves = {
    'player': "Status: It's your turn to make a move. Enter your command.",
    'computer': 'Status: Computer is about to make a move. Press Enter to continue...'
}


# double piece
def double(element):
    if element.count(element[0]) == 2:
        return True


# shuffle dominoes and give to players
def shuffle(deck):
    snake = [0, 0]
    turn_ = ''
    player_ = random.sample(deck, 7)
    for piece in player_:
        if piece in deck:
            deck.remove(piece)
        if double(piece):
            if piece[0] > snake[0]:
                snake = piece
    computer_ = random.sample(deck, 7)
    for piece in computer_:
        if piece in deck:
            deck.remove(piece)
        if double(piece):
            if piece[0] > snake[0]:
                snake = piece
    if snake in player_:
        player_.remove(snake)
        turn_ = 'computer'
    elif snake in computer_:
        computer_.remove(snake)
        turn_ = 'player'
    else:
        print('Reshuffle')

    return [snake], player_, computer_, deck, turn_


dominoes_snake, player, computer, stock, turn = shuffle(dominoes)


# show snake
def show_snake(data):
    if len(data) <= 6:
        print(*data, '\n')
    else:
        print(*data[0:3], '...', *data[-3:])


# AI implementation
def ai():
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    for i in computer:
        count_0 += i.count(0)
        count_1 += i.count(1)
        count_2 += i.count(2)
        count_3 += i.count(3)
        count_4 += i.count(4)
        count_5 += i.count(5)
        count_6 += i.count(6)
    for i in dominoes_snake:
        count_0 += i.count(0)
        count_1 += i.count(1)
        count_2 += i.count(2)
        count_3 += i.count(3)
        count_4 += i.count(4)
        count_5 += i.count(5)
        count_6 += i.count(6)

    data = {
        0: count_0,
        1: count_1,
        2: count_2,
        3: count_3,
        4: count_4,
        5: count_5,
        6: count_6,
    }

    scores = {}
    for i in computer:
        scores[str(i)] = data[i[0]] + data[i[1]]
    scores = sorted(scores.items(), key=lambda kv: kv[1])
    return scores


# make a move
def pc_move():
    run = True
    while run:
        scores = ai()
        for i in scores[:-1]:
            piece = legal_move(json.loads(i[0]), '+')
            if piece:
                dominoes_snake.append(piece)
                if piece in computer:
                    computer.remove(piece)
                else:
                    piece.reverse()
                    computer.remove(piece)
                    piece.reverse()

                return piece

            piece = legal_move(json.loads(i[0]), '-')
            if piece:
                dominoes_snake.insert(0, piece)
                if piece in computer:
                    computer.remove(piece)
                else:
                    piece.reverse()
                    computer.remove(piece)
                    piece.reverse()

                return piece

        if stock:
            piece = random.choice(stock)
            computer.append(piece)
            stock.remove(piece)
            return piece
        else:
            print('Status: The game is over. You won!')
            return None


# check move legality and reverse piece
def legal_move(domino, side):
    # define edges of snake
    left = dominoes_snake[0][0]
    right = dominoes_snake[-1][-1]
    # check if piece can be placed in selected position
    if side == '+':  # right
        # if last number of snake is in domino
        if right in domino:
            # place domino in correct position if needed
            if domino[1] == right:
                domino.reverse()
            return domino
    if side == '-':  # left
        # if last number of snake is in domino
        if left in domino:
            # place domino in correct position if needed
            if domino[0] == left:
                domino.reverse()
            return domino


# choice = input('Invalid input. Please try again.')
def player_move(choice):
    while True:
        # check if choice of piece is legal
        # check if choice is a digit
        try:
            choice = int(choice)
            # if choice is 0
            if choice == 0:
                if stock:
                    piece = random.choice(stock)
                    player.append(piece)
                    stock.remove(piece)
                else:
                    print('Status: The game is over. The computer won!')
                break
            # if choice is not 0
            else:
                side = '+'
                if choice < 0:
                    side = '-'
                    choice = choice * -1
                choice = choice - 1
                # check if choice is in range of player stock
                if choice < len(player):
                    # make move
                    piece = player[choice]
                    # check piece legality
                    test = legal_move(piece, side)
                    if test:
                        piece = test
                        player.remove(piece)
                        if side == '+':
                            dominoes_snake.append(piece)
                        else:
                            dominoes_snake.insert(0, piece)
                        break
                    else:
                        choice = input('Illegal move. Please try again.')
                else:
                    choice = input('Invalid input. Please try again.')
        except ValueError:
            choice = input('Invalid input. Please try again.')


# draw game field
def draw_game():
    print('=' * 70)
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(computer)}\n')
    show_snake(dominoes_snake)
    print('Your pieces:\n')
    for i_ in range(len(player)):
        print(f'{i_ + 1}:{player[i_]}')


# main function
def main():
    global dominoes_snake, player, computer, stock, turn
    run = True
    draw_game()
    while run:
        print(f'\n{moves[turn]}')
        if turn == 'player':
            player_move(input())
            turn = 'computer'
            if len(computer) == 0:
                print('Status: The game is over. The computer won!')
                break
        else:
            input()
            if pc_move():
                turn = 'player'
                if len(player) == 0:
                    print('Status: The game is over. You won!')
                    break
            else:
                print("Status: The game is over. It's a draw!")
                break
        draw_game()


# run game
if __name__ == '__main__':
    main()
