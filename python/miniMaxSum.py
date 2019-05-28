
def miniMaxSum(arr):
    minimum = arr[0]
    maximum = arr[0]
    total = 0

    for x in arr:
        total += x
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x


    return (total - maximum, total - minimum)


# M a i n   P r o g r a m

if miniMaxSum([7,9,3,1,5]) == (16,24):
    print("Sample Test 0 Passed")
else:
    print("Sample Test 0 Failed")

# Try your own list of numbers
v = [int(x) for x in input("numbers: ").split()]
print(' '.join([str(x) for x in miniMaxSum(v)]))


