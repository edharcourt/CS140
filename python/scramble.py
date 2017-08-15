import random,util

def scramble(word):
    tmp = ''

    while len(word) > 0:
        i = random.randrange(len(word))
        tmp = tmp + word[i]
        word = word[:i] + word[i+1:]

    return tmp


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

words = open('words.txt')

for word in words:
    if word[len(word)-1] == '\n':
        word = word[:len(word)-1]
    anagram = scramble(word)
    print("What word is this an anagram of?", anagram)
    guess = input('Enter word: ')

    if guess == word:
        print("Correct")
    else:
        print("Incorrect. The word is", '"' + word + '"')
        break