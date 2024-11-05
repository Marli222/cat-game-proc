import random

cat_attributes = {
    "intelligence": 0,
    "energy": 10,
    "weight": 4,
}

print("Welcome to my cat game!!!")

name = input("Enter name: ")
colour = input("Enter colour: ")

while True:
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
        cat_attributes['weight'] -= 1
    elif option == '2':
        print("You trained your cat!")
        cat_attributes['intelligence'] += 1
        cat_attributes['weight'] -= 1
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
        cat_attributes['energy'] += 1
    else:
        pass

    if cat_attributes['energy'] < 0 or cat_attributes['weight'] < 0:
        print("Your cat has gone to sleep forever.")
    if cat_attributes['weight'] > 17:
        print("Your cat died from being overweight :C")
    if cat_attributes['intelligence'] > 10:
        print("Your cat is very smart!")

    d100 = random.randint(1,100)
    if d100 == range(50,76):
        print("Your cat naps on your lap.")
        cat_attributes['energy'] += 2
    elif d100 == range(76,90):
        print("Your cat leaves you alone.")
    elif d100 == 91:
        print("Your cat brings back a dead rat for you <3")
    elif d100 == 92:
        print("Your cat bats the vase off the table.")
    elif d100 == 93:
        print("Your cat ate something it should'nt have.")
    elif d100 == range(94,101):
        print("Your cat randomly ascended to heaven.")
        quit()
