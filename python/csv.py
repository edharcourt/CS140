
print("Enter a comma separated list of numbers")
s = input("> ")

comma = s.find(',')
sum = 0
count = 0

while comma != -1:
    num = int(s[:comma])
    sum = sum + num
    count = count + 1
    s = s[comma+1:]
    comma = s.find(',')

sum = sum + int(s)
count = count + 1
avg = sum/count
print("Average: ", round(avg, 2))