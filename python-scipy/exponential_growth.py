import matplotlib.pyplot as plt, numpy

points = []
for i in range(1,11):
    points.append(94**i)

plt.figure(1)
plt.plot(points)
plt.ylabel('94^n')
plt.xlabel('i')
plt.show()