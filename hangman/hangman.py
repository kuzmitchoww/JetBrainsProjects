import random

word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hidden = ['-' for i in range(len(word))]
letters = []


def error_check(data):
    run_ = True
    while run_:
        if len(data) > 1 or not data:
            print('You should input a single letter')
            return None
        else:
            if data not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a lowercase English letter')
                return None
            else:
                return data


def run_game():
    tries = 8
    run = True

    while run:
        result = ''.join(hidden)

        if result == word:
            (print('\n', result))
            print(f"You guessed the word! {word}!\nYou survived!")
            break
        if tries < 1:
            print("You lost!")
            break

        print('\n', result)
        letter = error_check(input('Input a letter:'))
        while not letter:
            (print('\n', result))
            letter = error_check(input('Input a letter:'))

        if letter in word and letter not in hidden:
            letters.append(letter)
            indexes = [i for i, j in enumerate(word) if j == letter]
            for i in indexes:
                hidden[i] = letter
        elif letter in letters:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            letters.append(letter)
            tries -= 1


def loop():
    print('H A N G M A N')
    run = True
    while run:
        choice = input('Type "play" to play the game, "exit" to quit:')
        while choice != 'play' and choice != 'exit':
            choice = input('Type "play" to play the game, "exit" to quit:')
        if choice == 'play':
            run_game()
        if choice == 'exit':
            run = False


loop()
