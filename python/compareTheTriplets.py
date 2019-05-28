def compreTheTriplets(a, b):
    pass  # student fill in function here
    a_score = 0
    b_score = 0

    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
    return (a_score, b_score)


# M a i n   P r o g r a m

# Test Sample Input 0
if compreTheTriplets([5,6,7],[3,6,10]) == (1,1):
    print("Sample Input 0 Passed")
else:
    print("Sample Input 0 Failed")

# Test Sample Input 1
if compreTheTriplets((17,28,30),(99,16,8)) == (2,1):
    print("Sample Input 1 Passed")
else:
    print("Sample Input 1 Failed")


# Don't worry about how the main program works
#a = list(map(int,input("Alice:").split()))
a = [int(x) for x in input("Alice:").split()]
b = [int(x) for x in input("Bob:").split()]
print(' '.join([str(x) for x in compreTheTriplets(a,b)]))
