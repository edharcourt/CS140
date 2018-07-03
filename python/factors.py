
n = 83*199*83*17*163

factor = 2

while factor <= n:
    while n % factor == 0:
        print(factor)
        n = n / factor
    factor += 1