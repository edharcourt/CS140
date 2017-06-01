
# header
print("i     2^i")
print("=========")

i = 0
while i <= 10:
    print(i, '\t|', 2**i)
    i = i + 1


n = int(input("Enter n: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print(sum)