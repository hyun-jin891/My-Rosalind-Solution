
codon_table = {"F" : 2, "L" : 6, "I" : 3, "M" : 1, "V" : 4, "S" : 6, "P" : 4, "T" : 4, "A" : 4, "Y" : 2, "H" : 2, "Q" : 2, "N" : 2, "K" : 2, "D" : 2, "E" : 2, "C" : 2, "W" : 1, "R" : 6, "G" : 4}

name = input()
f = open(name, 'r')

aaSeq = ""

for line in f.readlines():
    aaSeq += line[:-1]


case = 1

for i in range(len(aaSeq)):
    aa = aaSeq[i]
    case *= codon_table[aa]
    case %= 1000000

print((case * 3) % 1000000)
f.close()
    


