def maxOf3(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print(maxOf3(5,9,3))