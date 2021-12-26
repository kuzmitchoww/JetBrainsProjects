from animals import animals

exit_ = False

while not exit_:
    choice = (input("Please enter the number of the habitat you would like to view:"))
    if choice != "exit":
        print(animals[int(choice)])
    else:
        print("See you later!")
        exit_ = True