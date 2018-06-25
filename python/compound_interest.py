# the value of an investment
# c - initial investment
# r - interest rate
# n - number of compounds per year
# t - number of years
def interest(c,r,n,t):
    p = c*(1 + r/n)**(t*n)
    return p

print(interest(1000,.01,1,1))