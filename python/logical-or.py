import random

d1 = random.randrange(6) + 1
d2 = random.randrange(6) + 1

if d1 == 1:
    print("one")
elif d2 == 1:
    print("one")

if d1 == 1 or d2 == 1:
    print("one")

if d1 == 1 and d2 == 1:
    print("snake eyes")

if (d1 == 1 or d2 == 1) and d1 != d2:
    print("exactly one, one")

if (d1 == 1 or d2 == 1) and (d1 != 1 or d2 != 1):
    print("exactly one, one")