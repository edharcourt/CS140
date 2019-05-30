"""
Hackerrank problem

https://www.hackerrank.com/work/library/hackerrank?question=569444&view=question

Shortest Substring
Given a string comprised of lowercase letters in the range ascii[a-z], determine the length of the smallest substring that contains all of the letters present in the string.



For example, given the string s = dabbcabcd, the list of all characters in the string is [a, b, c, d].  Two of the substrings that contain all letters are dabbc and abcd.  The shortest substring containing all the letters is 4 characters long, abcd.


"""

def shortestSubstring(s):

    unique_chars = ""

    for ch in s:
        if ch not in unique_chars:
            unique_chars += ch


    sub = ""
    for ch in s:


print(shortestSubstring("antidisestablishmentarianism"))
print(shortestSubstring("hippopotomonstrosesquippedaliophobia"))
