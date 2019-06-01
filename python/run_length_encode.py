
# run length encode a string s
def run_length_encode(s):
    tmp = ""
    prev = s[0]
    cnt = 0

    for ch in s[1:]:
        if prev == ch:
           cnt += 1
        else:
            tmp += prev
            if cnt > 0:
                tmp += str(cnt+1)
                cnt = 0

        prev = ch


    tmp += prev
    if cnt > 0:
        tmp += str(cnt + 1)

    return tmp


# M a i n    P r o g r a m

if run_length_encode("aaaaaa") == 'a6':
    print('Test 0 Passed')
else:
    print('Test 0 Failed')

if run_length_encode("cccaagtaaa") == 'c3a2gta3':
    print('Test 1 Passed')
else:
    print('Test 1 Failed')

if run_length_encode("gggctttttttttcgacccaaa") == 'g3c1t9c1g1a1c3a3':
    print('Test 2 Passed')
else:
    print('Test 2 Failed')

f = open("ecoli.txt")
l = f.readline()
rle_l =  run_length_encode(l)
print(len(l), len(rle_l))