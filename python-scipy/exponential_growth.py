import matplotlib.pyplot as plt, numpy

points = []
i = 1
while i <= 10:
    points.append(94**i)
    i = i + .01

plt.figure(1)
plt.plot(points)
plt.ylabel('94^n')
plt.xlabel('i')
plt.show()

i = 1
sum = 0
while i <= 10:
    sum = sum + 94**i
    i = i + 1

print(sum)

i = 1
sum = 0
pow94 = 94
while i <= 10:
    sum = sum + pow94
    pow94 = pow94 * 94
    i = i + 1

print(sum)