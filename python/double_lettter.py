
f = open("large_wordlist.txt")

def count_double_letters(word):

    prev= ""
    cnt = 0
    for ch in word:
        if prev == ch:
            cnt = cnt + 1

        prev = ch

    return cnt


print(count_double_letters('mississippi'))

for word in f:
    if count_double_letters(word) >= 4:
        print(word)
