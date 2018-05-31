import random,util, string

def scramble(word):
    tmp = ''

    while len(word) > 0:
        i = random.randrange(len(word))
        tmp = tmp + word[i]
        word = word[:i] + word[i+1:]

    return tmp


def encrypt(cleartext, key):

    alphabet = string.ascii_lowercase
    ciphertext = ''

    for ch in cleartext:
        ciphertext = ciphertext + key[alphabet.find(ch)]

    return ciphertext


def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase

    cleartext = ''

    for ch in ciphertext:
        cleartext = cleartext + alphabet[key.find(ch)]

    return cleartext

key = scramble(string.ascii_lowercase)

secret = encrypt("attackatdawn", key)
print(secret)
print(decrypt(secret, key))