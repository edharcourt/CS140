import random

n = int(input("Enter number of times to toss coin: "))

i = 0
heads = 0
tails = 0

toss = random.randrange(2)

if toss == 0:
    heads = heads + 1
else:
    tails = tails + 1


