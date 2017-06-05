import random

d = random.randrange(6) + 1
if d == 1:
    print("one")
else:
    if d == 2:
        print("two")
    else:
        if d == 3:
            print("three")
        else:
            if d == 4:
                print("four")
            else:
                if d == 5:
                    print("five")
                else:
                    print("six")


d = random.randrange(6) + 1
if d == 1:
    print("one")
elif d == 2:
    print("two")
elif d == 3:
    print("three")
elif d == 4:
    print("four")
elif d == 5:
    print("five")
else:
    print("six")