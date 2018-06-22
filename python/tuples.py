name = ("Harry", "Potter")
print(name[1], name[0])
print(len(name))

grades = (98, 78, 72, 100, 85, 76)

sum = 0
for g in grades:
    sum += g

avg = sum / len(grades)
print("The average is", round(avg,2))