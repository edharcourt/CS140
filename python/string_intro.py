s = 'antidisestablishmentarianism'
print(len(s))

a_count = 0

for ch in s:
    if ch == 'a':
        a_count = a_count + 1

print(a_count)

a_count = 0
for i in range(len(s)):
    if s[i] == 'a':
        a_count = a_count + 1

print(a_count)

def reverse(s):
    tmp = ""
    for ch in s:
        tmp = ch + tmp

    return tmp

print(reverse('hello'))

def palindrome(s):
   if s == reverse(s):
       return True
   else:
       return False

print(palindrome('racecar'))
print(palindrome('kayak'))
print(palindrome('madam'))
print(palindrome('harry'))