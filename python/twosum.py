# This is a problem #1 from the Daily Coding Problem

def twoSum(nums, k):
    for x in nums:
        for y in nums:
            if x + y == k:
                return True

    return False


# Try your own inputs
print(twoSum([4,9,33,2,16], 25))

print(twoSum([4,9,33,2,16], 14))

# Try your own k and list
k = int(input("k: "))
nums = [int(x) for x in input("Numbers:").split()]
print(twoSum(nums,k))
