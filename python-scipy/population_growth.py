import matplotlib.pyplot as plt, numpy

p = 7.5e9    # initial population 7.5 billion
i = 0        # counter
r = .011     # growth rate 1.1%
n = int(input("Enter a number of years: "))
pop = [p]

while i < n:
    p = p * (1 + r)
    i = i + 1
    r = r - .00025
    pop.append(p)

plt.figure(1)
plt.plot(pop)
plt.ylabel('population')
plt.xlabel('t')
plt.show()

print("Final population: ", int(p))