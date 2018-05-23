
def linecount(fname):
    f = open(fname)
    count = 0
    for _ in f:
        count = count + 1
    f.close()
    return count

# Main program
name = 'words.txt'
print('File', name, 'has', linecount(name), 'lines')
