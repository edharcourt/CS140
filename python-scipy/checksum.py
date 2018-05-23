
data = int(input("Enter and integer: "))

def checksum(n):
    sum = 0

    while n > 0:
        sum = sum + (n % 10)
        n = n // 10
    return sum % 10

print("The checksum of ", data, " is ", checksum(data))
