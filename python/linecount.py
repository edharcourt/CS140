
f = open('words.txt')

count = 0
for _ in f:
    count = count + 1

print("words.txt has", count, "lines")
