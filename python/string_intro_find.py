s1 = 'antidisestablishmentarianism'
s2 = 'hippopotomonstrosesquipedaliophobia'
print(s1.find('establish'))
print(s1.find('hippo'))
print(s2.find('po'))
print(s2.find('po',4))

start = s2.find('po')
print(s2.find('po', start+1))

s = input("Enter a string: ")
count = 0
loc = s.find('is')
while loc != -1:
    count = count + 1
    loc = s.find('is',loc+1)

print('"is" appears', count, "times in",s)
print(s.count('is'))
