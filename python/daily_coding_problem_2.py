"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def dcp2(l):

    prod = 1
    for n in l:
        prod *= n

    for i in range(len(l)):
        l[i] = prod//l[i]

    return l



# What if we can't use division
def dcp2_nodiv(l):

    res = []
    for i in range(len(l)):

        # multiply values to the left of i
        prod1 = 1
        for j in range(i):
            prod1 *= l[j]

        # multiply values to the right of i
        prod2 = 1
        for j in range(i+1, len(l)):
            prod2 *= l[j]

        res.append(prod1*prod2)

    return res


print(dcp2([1,2,3,4,5]))
print(dcp2_nodiv([1,2,3,4,5]))