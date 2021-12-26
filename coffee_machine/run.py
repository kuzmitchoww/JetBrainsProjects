# in machine
water = 400
milk = 540
beans = 120
cups = 9
money = 550


class Machine:
    def __init__(self, w, m, b, c, mn):
        self.water = w
        self.milk = m
        self.beans = b
        self.cups = c
        self.money = mn

    def __repr__(self):
        return (f"The coffee machine has:\n"
                f"{self.water} of water\n"
                f"{self.milk} of milk\n"
                f"{self.beans} of coffee beans\n"
                f"{self.cups} of disposable cups\n"
                f"${self.money} of money")

    def espresso(self):
        amount = min([self.water // 250, self.beans // 16, self.cups // 1])
        if amount > 0:
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
            print('I have enough resources, making you a coffee!')
        else:
            ingredients = [self.water, self.beans, self.cups]
            for i in [self.water // 250, self.beans // 16, self.cups // 1]:
                if i == 0:
                    print(f'Sorry, not enough {ingredients[i]}!')

    def latte(self):
        amount = min([self.water // 350, self.milk // 75, self.beans // 20, self.cups // 1])
        if amount > 0:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
        else:
            ingredients = [self.water, self.milk, self.beans, self.cups]
            for i in [self.water // 250, self.milk // 75, self.beans // 16, self.cups // 1]:
                if i == 0:
                    print(f'Sorry, not enough {ingredients[i]}!')

    def cappuccino(self):
        amount = min([self.water // 200, self.milk // 100, self.beans // 12, self.cups // 1])
        if amount > 0:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
        else:
            ingredients = [self.water, self.milk, self.beans, self.cups]
            for i in [self.water // 200, self.milk // 100, self.beans // 12, self.cups // 1]:
                if i == 0:
                    print(f'Sorry, not enough {ingredients[i]}!')

    def take(self):
        print(f'I gave you ${self.money}\n')
        self.money = 0

    def buy(self):
        drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if drink == '1':
            self.espresso()
        elif drink == '2':
            self.latte()
        elif drink == '3':
            self.cappuccino()
        else:
            print("Incorrect choice")

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def run(self):
        while True:
            action_ = input('Write action (buy, fill, take, remaining, exit):\n')
            if action_ == 'buy':
                self.buy()
            elif action_ == 'fill':
                self.fill()
            elif action_ == 'take':
                self.take()
            elif action_ == 'remaining':
                print(self.__repr__())
            else:
                break


machine = Machine(water, milk, beans, cups, money)
machine.run()
