"""
a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
"""

import string, random

def encrypt(cleartext, otp):

    alphabet = string.printable
    alphabet = string.ascii_lowercase
    ciphertext = ''

    for i in range(len(cleartext)):
        ciphertext += alphabet[(alphabet.find(cleartext[i]) +
                                alphabet.find(otp[i])) % len(alphabet)]

    return ciphertext

def decrypt(ciphertext, otp):

    alphabet = string.printable
    alphabet = string.ascii_lowercase
    cleartext = ''

    for i in range(len(ciphertext)):
        cleartext += alphabet[(alphabet.find(ciphertext[i]) -
                               alphabet.find(otp[i])) % len(alphabet)]

    return cleartext

def GenOneTimePad(n):
    pad = ''
    alphabet = string.printable
    alphabet = string.ascii_lowercase

    for i in range(n):
        pad += alphabet[random.randrange(len(alphabet))]

    return pad

otp = GenOneTimePad(20)

print(decrypt(encrypt('hello', otp), otp))
print(encrypt("bazooka", otp))
print(otp)