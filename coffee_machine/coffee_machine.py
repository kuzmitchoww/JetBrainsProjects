class Machine:
    def __init__(self):

        self.ingredients = {
            'water': 400,
            'milk': 540,
            'coffee beans': 120,
            'disposable cups': 9,
            'money': 550
        }

        self.recipe = {
            'espresso': {
                'water': [self.ingredients['water'] // 250, 250],
                'milk': [1000, 0],
                'coffee beans': [self.ingredients['coffee beans'] // 16, 16],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [4]
            },
            'latte': {
                'water': [self.ingredients['water'] // 350, 350],
                'milk': [self.ingredients['milk'] // 75, 75],
                'coffee beans': [self.ingredients['coffee beans'] // 20, 20],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [7]
            },
            'cappuccino': {
                'water': [self.ingredients['water'] // 200, 200],
                'milk': [self.ingredients['milk'] // 100, 100],
                'coffee beans': [self.ingredients['coffee beans'] // 12, 12],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [6]
            }
        }

    def update(self):
        self.recipe = {
            'espresso': {
                'water': [self.ingredients['water'] // 250, 250],
                'milk': [1000, 0],
                'coffee beans': [self.ingredients['coffee beans'] // 16, 16],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [4]
            },
            'latte': {
                'water': [self.ingredients['water'] // 350, 350],
                'milk': [self.ingredients['milk'] // 75, 75],
                'coffee beans': [self.ingredients['coffee beans'] // 20, 20],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [7]
            },
            'cappuccino': {
                'water': [self.ingredients['water'] // 200, 200],
                'milk': [self.ingredients['milk'] // 100, 100],
                'coffee beans': [self.ingredients['coffee beans'] // 12, 12],
                'disposable cups': [self.ingredients['disposable cups'] // 1, 1],
                'money': [6]
            }
        }

    def machine_representation(self):
        print('The coffee machine has:\n')
        for key, value_ in self.ingredients.items():
            if key != 'money':
                print(f'{value_} of {key}')
            else:
                print(f'${value_} of {key}')

    def sell_coffee(self, coffee_type):
        coffees = ['espresso', 'latte', 'cappuccino']
        coffee = self.recipe[coffees[coffee_type]]
        max_amount = [i[0] for i in list(coffee.values())]
        try:
            assert 0 not in max_amount, f'Sorry, not enough {list(coffee.keys())[max_amount.index(0)]}\n '
            print('I have enough resources, making you a coffee!\n')
            for key, val in self.ingredients.items():
                if key != 'money':
                    self.ingredients[key] = val - coffee[key][1]
                else:
                    self.ingredients[key] = val + coffee[key][-1]
            self.update()

        except AssertionError as msg:
            print(msg)

    def take(self):
        print(f'I gave you ${self.ingredients["money"]}\n')
        self.ingredients['money'] = 0

    def action(self):
        go = True
        while go:
            action_ = input('Write action (buy, fill, take, remaining, exit):\n')
            if action_ == 'buy':
                act = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if act != 'back':
                    self.sell_coffee(int(act) - 1)
                else:
                    continue
            elif action_ == 'take':
                self.take()
            elif action_ == 'fill':
                self.ingredients['water'] += int(input('Write how many ml of water you want to add:'))
                self.ingredients['milk'] += int(input('Write how many ml of milk you want to add:'))
                self.ingredients['coffee beans'] += int(input('Write how many grams of coffee beans you want to add:'))
                self.ingredients['disposable cups'] += int(input('Write how many disposable coffee cups you want to '
                                                                 'add:'))
                self.update()
            elif action_ == 'remaining':
                self.machine_representation()
            else:
                return False
            print()

    def run_(self):
        run = True
        while run:
            if not self.action():
                run = False
            else:
                self.machine_representation()


if __name__ == '__main__':
    m = Machine()
    m.run_()
