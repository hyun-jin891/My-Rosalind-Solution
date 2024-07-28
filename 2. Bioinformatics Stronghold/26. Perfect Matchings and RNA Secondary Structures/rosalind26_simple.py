from math import factorial

def AU_count(seq):
    res = 0
    
    for i in range(len(seq)):
        if seq[i] == 'A' or seq[i] == 'U':
            res += 1
    
    return res


name = input()
f = open(name, 'r')

f.readline()
rnaSeq = ""

for line in f.readlines():
    rnaSeq += line[:-1]

AU_pair = AU_count(rnaSeq)
GC_pair = len(rnaSeq) - AU_pair


print(factorial(AU_pair//2) * factorial(GC_pair//2))

f.close()