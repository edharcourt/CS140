import string
def encrypt(clear,shift):

    alpha = string.printable
    cipher = ''

    for ch in clear:
        chpos = alpha.find(ch)
        cipherpos = (chpos + shift) % len(alpha)
        cipher = cipher + alpha[cipherpos]
    return cipher


print(encrypt("Attack at dawn!", 13))
print(encrypt("NGGnpx7nG7qnJA.", -13))