import random


# define main game loop function
def run():
    words = ['python', 'java', 'kotlin', 'javascript']  # create list with words to choose
    word = random.choice(words)  # set random word from list to guess
    hidden = ["-" for x in range(len(word))]  # creates hidden word replacing all unsolved letters by "-"
    used = []  # list of used letters
    tries = 8  # set tries to 8

    # run loop
    while True:
        print(''.join(hidden))
        letter = input("Input a letter:")
        if len(letter) == 1:  # check if input is single letter
            if letter.islower():  # check if letter is lowercase
                if letter not in word and letter not in used:  # if selected letter is incorrect and was not selected yet
                    tries -= 1  # decrease tries by 1 every iteration in "while" loop
                    if tries == 0:  # break loop if there are no more tries, print loose message
                        print("That letter doesn't appear in the word\nYou lost!")
                        break
                    else:
                        print("That letter doesn't appear in the word\n")
                elif letter in used:  # if selected letter is already guessed
                    print("You've already guessed this letter\n")
                else:  # if selected letter is correct
                    count = 0  # create counter to get letter index in word
                    for i in word:  # iterate through word to get letter index and replace "-" in hidden by guessed letter
                        if i == letter:
                            hidden[count] = letter
                        count += 1
                    print()
                used.append(letter)  # add letter to used letters list
            else:
                print("Please enter a lowercase English letter\n")
        else:
            print("You should input a single letter\n")
        if "-" not in hidden:  # break loop if there are no more letters to guess, print win message
            print(f'{word}\nYou guessed the word!\nYou survived!\n')
            select()
            break


# define user selection function
def select():
    return input('Type "play" to play the game, "exit" to quit:\n')


print("H A N G M A N\n")

# loop selection till "play" is not selected
while True:
    if select() == "play":
        run()
        break
    else:
        select()
