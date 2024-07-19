



seq1 = ""
seq2 = ""
seq1 = "0" + seq1
seq2 = "0" + seq2

name = input()
f = open(name, 'r')
f.readline()
tempSeq = ""

for line in f.readlines():
    if line[0] == '>':
        seq1 += tempSeq
        tempSeq = ""
    else:
        tempSeq += line[: -1]

seq2 += tempSeq
        
dp = [[0 for i in range(len(seq1))] for j in range(len(seq2))]

for j in range(1, len(seq2)):
    for i in range(1, len(seq1)):
        if seq1[i] == seq2[j]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

shared_motif = ""

current_j = len(seq2) - 1
current_i = len(seq1) - 1

while current_j >= 1 and current_i >= 1:
    if dp[current_j][current_i] == dp[current_j - 1][current_i]:
        current_j -= 1
    elif dp[current_j][current_i] == dp[current_j][current_i - 1]:
        current_i -= 1
    else:
        shared_motif = seq1[current_i] + shared_motif
        current_j -= 1
        current_i -= 1

print(shared_motif)
f.close()           
