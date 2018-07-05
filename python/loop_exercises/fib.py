
# Compute the 100th Fibonacci number

prev = 0
curr = 1
n = 2

while n < 100:
    n += 1
    tmp = curr
    curr = curr + prev
    prev = tmp
    print(n,curr)

