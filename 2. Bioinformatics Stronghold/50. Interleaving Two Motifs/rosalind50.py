def form_table(seq1, seq2):
    table = [[0 for i in range(len(seq1))] for i in range(len(seq2))]
    for i in range(1, len(seq2)):
        for j in range(1, len(seq1)):
            if seq1[j] == seq2[i]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])
    return table
                
def find_superseq(table, seq1, seq2):
    superseq = ""
    i = len(seq2) - 1
    j = len(seq1) - 1
    
    while i > 0 or j > 0:
        if seq1[j] != seq2[i]:
            if table[i][j] == table[i][j - 1]:
                superseq = seq1[j] + superseq
                j = j - 1
            elif table[i][j] == table[i - 1][j]:
                superseq = seq2[i] + superseq
                i = i - 1
        else:
            superseq = seq1[j] + superseq
            i = i - 1
            j = j - 1
    
    return superseq
    

name = input()
f = open(name, 'r')

seq1 = f.readline()[:-1]
seq1 = "X" + seq1
seq2 = f.readline()[:-1]
seq2 = "X" + seq2

dp = form_table(seq1, seq2)
superseq = find_superseq(dp, seq1, seq2)

print(superseq)

f.close()






