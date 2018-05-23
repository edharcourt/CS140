import random
chips = 1000
while chips > 0 and chips < 2000:
    toss = random.randrange(2)

    if toss == 0:
        chips = chips + 1
    else:
        chips = chips - 1
    
