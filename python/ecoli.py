
ecoli = open("ecoli.txt")

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for line in ecoli:
    for bp in line:
        if bp == 'a':
            a_count = a_count + 1
        elif bp == 'c':
            c_count = c_count + 1
        elif bp == 'g':
            g_count = g_count + 1
        elif bp == 't':
            t_count = t_count + 1

total = a_count + c_count + g_count + t_count
print('length:', total)
print('a: ', a_count, ', ', round(a_count/total * 100, 1), '%', sep='')
print('c: ', c_count, ', ', round(c_count/total * 100, 1), '%', sep='')
print('g: ', g_count, ', ', round(g_count/total * 100, 1), '%', sep='')
print('t: ', t_count, ', ', round(t_count/total * 100, 1), '%', sep='')