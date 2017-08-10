import random

def scramble(word):
    tmp = ''

    while len(word) > 0:
        i = random.randrange(len(word))
        tmp = tmp + word[i]
        s = word[:i] + word[i+1:]

    return tmp


print(scramble('python'))
'''
j = 0
sum = 0
while j < 1000:
    i = 0
    while 'python' != scramble('python'):
        i = i + 1
    j += 1
    sum = sum + i

print(round(sum/j,1))
'''