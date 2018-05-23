

def find_possible_genes(dna:str):

    # find the location of 'atg'.
    start = dna.find('atg')
    count = 0
    while start > -1:

        for i in range(start+3, len(dna)-3, 3):
            if dna[i:i+3] in ['taa', 'tag', 'tga'] and \
                    (i - start) % 3 == 0:
                print(start, i, i - start)
                count += 1
                break

        start = dna.find('atg',start+1)
    print(count)


if __name__ == "__main__":
    f = open('ecoli.txt')

    dna = f.readline(1000)
    print(dna)
    find_possible_genes(dna)