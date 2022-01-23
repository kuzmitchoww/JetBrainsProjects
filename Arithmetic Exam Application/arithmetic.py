# write your code here
from random import choice, randint


class Calculator:
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 1
        self.operand = '+'
        self.data = f'{self.num_1}{self.operand}{self.num_2}'

        self.calculations = {
            '+': self.add(),
            '-': self.extract(),
            '*': self.multiply()
        }
        self.result = self.calculations[self.operand]
        self.user_input = ''
        self.mark = 0
        self.randomise_lvl_1()
        self.file = 'results.txt'
        self.choice = 0
        self.descriptions = {
            1: '(simple operations with numbers 2-9)',
            2: '(integral squares of 11-29)'
        }

    def check_format(self, user_input):
        if user_input.isdigit() or user_input.strip('-').isdigit():
            self.user_input = int(user_input)
            return True
        else:
            return False

    def randomise_lvl_1(self):
        self.num_1 = randint(2, 9)
        self.num_2 = randint(2, 9)
        self.operand = choice(['+', '-', '*'])
        self.data = f'{self.num_1} {self.operand} {self.num_2}'
        self.calculations = {
            '+': self.add(),
            '-': self.extract(),
            '*': self.multiply()
        }
        self.result = self.calculations[self.operand]

    def randomise_lvl_2(self):
        self.num_1 = randint(11, 29)
        self.num_2 = self.num_1
        self.operand = '*'
        self.data = {self.num_2}
        self.calculations = {
            '+': self.add(),
            '-': self.extract(),
            '*': self.multiply()
        }
        self.result = self.calculations[self.operand]

    def lvl_choice(self):
        run = True
        while run:
            print('Which level do you want? Enter a number:')
            print('1 - simple operations with numbers 2-9')
            print('2 - integral squares of 11-29')
            choice_ = input()
            if choice_ not in ['1', '2']:
                print('Incorrect format.')
            else:
                self.choice = int(choice_)
                break

    def lvl_1(self):
        count = 5
        while count != 0:
            print(self.data)
            test = input()
            while not self.check_format(test):
                print('Wrong format! Try again.')
                test = input()
            if self.user_input == self.result:
                print('Wright!')
                self.mark += 1
            else:
                print('Wrong!')
            count -= 1
            self.randomise_lvl_1()
        return True

    def lvl_2(self):
        count = 5
        while count != 0:
            self.result = randint(11, 29)
            print(self.result)
            test = input()
            while not self.check_format(test):
                print('Wrong format! Try again.')
                test = input()
            if self.user_input == self.result * self.result:
                print('Wright!')
                self.mark += 1
            else:
                print('Wrong!')
            count -= 1
            self.randomise_lvl_2()
        return True

    def save_result(self):
        name = input('What is your name?')
        with open('results.txt', 'a+') as f:
            f.write(f'{name}: {self.mark}/5 in level {self.choice} {self.descriptions[self.choice]}')
            f.close()
        print('The results are saved in "results.txt".')

    def add(self):
        return self.num_1 + self.num_2

    def extract(self):
        return self.num_1 - self.num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def run(self):
        go = True
        while go:
            self.lvl_choice()
            if self.choice == 1:
                self.lvl_1()
            else:
                self.lvl_2()
            if input(f'Your mark is {self.mark}/5. Would you like to save the result? Enter yes or no.') \
                    in ['y', 'Y', 'YES', 'Yes']:
                self.save_result()
                go = False
            else:
                go = False


calc = Calculator()
calc.run()
