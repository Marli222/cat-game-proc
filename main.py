cat_attributes = {
    "intelligence": 0,
    "energy": 10,
    "weight": 4,
}

print("Welcome to my cat game!!!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("Enter colour: ")

# start the while loop
while True:
    # Finish the string below
    option = input("""What would you like to do? 
                   1. Play with your cat 
                   2. Train your cat 
                   3. Show stats
                   4. Feed your cat
                   5. Put your cat to sleep
                   """)
    if option == '1':
        print("You played with your cat!")
        cat_attributes['energy'] -= 1
        pass
    elif option == '2':
        print("You trained your cat!")
        cat_attributes['intelligence'] += 1
    elif option == '3':
        print("Your Stats:")
        for x in cat_attributes:
            print(f"Your cat's {x} is {cat_attributes[x]}")
    elif option == '4':
        print("You feed your cat!")
        cat_attributes['weight'] += 1
        cat_attributes['energy'] += 1
    elif option == '5':
        print("Your cat is asleep!")
        cat_attributes['energy'] -= 1
    else:
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        pass
    # elif ...
