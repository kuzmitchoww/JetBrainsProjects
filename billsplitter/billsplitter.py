# write your code here
import random

amount = int(input('Enter the number of friends joining (including you):\n'))
friends = {}

if amount <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')

    for friend in range(amount):
        friends.update({input(''): 0})
    print()
    bill = int(input('Enter the total bill value:\n'))
    for key in friends.keys():
        friends[key] = round(bill / amount, 2)
    print()
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    friend_luck = random.choice(list(friends.keys()))
    print()
    print('No one is going to be lucky' if lucky == 'No' else f'{friend_luck} is the lucky one!')
    if lucky == 'Yes':
        for key in friends.keys():
            friends[key] = round(bill / (amount - 1), 2)
        friends[friend_luck] = 0
    print()
    print(friends)
