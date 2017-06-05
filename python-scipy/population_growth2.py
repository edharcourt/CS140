
p = 7.5e9    # initial population 7.5 billion
i = 0        # counter
r = .011     # growth rate 1.1%

while p < 10e9:
    p = p * (1 + r)
    i = i + 1
    r = max(.001, r - .00025)

print(i, "years to 10 billion")