def hamming_dist(seq1, seq2):
    res = 0
    
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res += 1
    
    return res



seqs = []
name = input()
f = open(name, 'r')

f.readline()
tempSeq = ""

for line in f.readlines():
    if line[0] == '>':
        seqs.append(tempSeq)
        tempSeq = ""
    else:
        tempSeq += line[:-1]

seqs.append(tempSeq)

for i in range(len(seqs)):
    seq1 = seqs[i]
    for j in range(len(seqs)):
        if i == j:
            print(0.00000, end=" ")
        else:
            seq2 = seqs[j]
            hamming_distance = hamming_dist(seq1, seq2)
            print(hamming_distance/len(seq1), end = " ")
    
    print()
        

f.close()
