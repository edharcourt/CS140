import random

# place a goat behind a door. Or assign
# a door to goat 1
goat1 = random.randrange(1,4)

goat2 = random.randrange(1,4)

while goat1 == goat2:
    goat2 = random.randrange(1,4)

# how did the loop terminate?

# assign a car to the door that is not the
# same a goat 1 or goat 2
car = random.randrange(1,4)

while car == goat1 or car == goat2:
    car = random.randrange(1,4)

# What is true?
# car != goat1 != goat2
# print(goat1,goat2,car)
choice = int(input("Choose a door: "))

# figure out how to show a goat
# to the contestant
if choice == goat1:
    show = goat2
    switch = car
elif choice == goat2:
    show = goat1
    switch = car
else:
    show = goat1
    switch = goat2

print("There is a goat in door", show)

switch_doors = input("Do you want to switch?(y/n): ")
if switch_doors == 'y' or switch_doors == 'Y':
    choice = switch

# Did they win?
if choice == car:
    print("You won a car!")
else:
    print("You won a goat!")