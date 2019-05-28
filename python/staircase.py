

def staircase(n):

    for i in range(n):
        print(' '*(n - i - 1) + '#'*(i+1))


# M a i n    P r o g r a m
staircase(int(input('n: ')))