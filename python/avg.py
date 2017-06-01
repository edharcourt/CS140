
n   = float(input("Enter a number: "))
i   = 0
sum = 0

while n >= 0:
    i = i + 1
    sum = sum + n
    n = float(input("Enter a number: "))

average = sum / i
print("The average is ", round(average, 2))
