import random

n = int(input("Enter number of times to toss coin: "))

i = 0
heads = 0
tails = 0
in_a_row = 0
in_a_row_count = 0

while i < n:
    toss = random.randrange(2)

    if toss == 0:
        heads = heads + 1
        in_a_row = in_a_row + 1
    else:
        tails = tails + 1
        in_a_row = 0

    if in_a_row == 10:
        in_a_row_count += 1

    i = i + 1

print("Heads: ", heads)
print("Tails: ", tails)
print("Number of ten in a row: ", in_a_row_count)
