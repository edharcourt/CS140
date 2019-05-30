"""
Cracking the Coding Interview 6th ed. problem 1.1

Implement an algorithm to determine if a string has all unique characters
"""

def uniqueChars(s):

    unique_chars = ""

    for ch in s:
        if ch not in unique_chars:
            unique_chars += ch

    return unique_chars

def allUniqueChars(s):

    unique_chars = ""

    for ch in s:
        if ch not in unique_chars:
            unique_chars += ch
        else:
            return False
    return True

def allUniqueChars2(s):

    unique_chars = ""

    for ch in s:
        isin = False
        for x in unique_chars:
            if ch == x:
                isin = True
        if isin:
            return False
        else:
            unique_chars += ch
    return True


# M a i n   P r o g r a m
if set(uniqueChars("antidisestablishmentarianism")) == set("antidseblhmr"):
    print("Test passed")
else:
    print("Test failed")

if set(uniqueChars("hippopotomonstrosesquippedaliophobia")) == set("hipotmnsrequdalb"):
    print("Test passed")
else:
    print("Test failed")

print(allUniqueChars2('abcdefg'))
print(allUniqueChars2('babcdefg'))
print(allUniqueChars('abcdefg'))
print(allUniqueChars('babcdefg'))
