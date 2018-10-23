
sum = 0
for i in range(8,3):
    sum += i
print(sum)


for i in range(8,3,-1):
    print(i,end="")

for i in range(3,8):
    print(i,end="")

print()
print('i','\t','j')
print('-','\t','-')
for i in range(4):
    for j in range(3):
        print(i,'\t',j)
print('=============')
for i in range(4):
    for j in range(i,3):
        print(i,'\t',j)
