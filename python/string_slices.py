
print("Enter three numbers separated by a comma")
s = input("> ")
comma1 = s.find(',')
comma2 = s.find(',', comma1+1)
num1 = int(s[:comma1])
num2 = int(s[comma1+1:comma2])
num3 = int(s[comma2+1:])

avg = (num1 + num2 + num3) / 3
print("Average:", round(avg,2))
