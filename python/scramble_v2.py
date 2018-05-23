import random,util

def scramble(word):
    tmp = ''

    while len(word) > 0:
        i = random.randrange(len(word))
        tmp = tmp + word[i]
        word = word[:i] + word[i+1:]

    return tmp


words = open('words.txt')

lost = False
done = False

while not lost and not done:
    word = words.readline()
    if len(word) == 0:
        done = True
    else:
        word = word[:len(word)-1]
        anagram = scramble(word)
        print("What word is this an anagram of?", anagram)
        guess = input('Enter word: ')

        if guess == word:
            print("Correct")
        else:
            print("Incorrect. The word is", '"' + word + '"')
            lost = True


if not lost:
    print("You win!")

