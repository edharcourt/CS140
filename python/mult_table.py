
for i in range(1,10):
    for j in range(1,10):
        print(i * j, "\t", end="")
    print()

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i * j, "\t", end="")
        j = j + 1
    print()
    i = i + 1