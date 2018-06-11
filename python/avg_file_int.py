
f = open("grades.txt")

total = 0
count = 0

for grade in f:
    total += int(grade)
    count += 1

print("The average is", round(total/count, 1))