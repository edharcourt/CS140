f = open('grades.txt')
grades = []

for grade in f:
    grades.append(float(grade))

grades.sort()

if len(grades) % 2 == 1:
    median = grades[len(grades)//2]
else:
    mid1 = grades[len(grades)//2 - 1]
    mid2 = grades[len(grades)//2]
    median = (mid1 + mid2) / 2

print('Median:', round(median, 1))