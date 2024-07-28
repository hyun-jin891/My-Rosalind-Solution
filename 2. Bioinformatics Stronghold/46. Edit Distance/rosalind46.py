seq1 = ""
seq2 = ""

name = input()
f = open(name, 'r')

f.readline()
flag = False

for line in f.readlines():
    if line[0] == '>':
        flag = True
        continue
    if flag:
        seq2 += line[:-1]
    else:
        seq1 += line[:-1]
          
seq1 = "0" + seq1
seq2 = "0" + seq2

dp = [[0 for i in range(len(seq1))] for j in range(len(seq2))]
direction = [(1, 1), (1, 0), (0, 1)]

for j in range(len(seq2) - 1, -1, -1):
    for i in range(len(seq1) - 1, -1, -1):
        if j == len(seq2) - 1 and i == len(seq1) - 1:
            continue
        
        if j == len(seq2) - 1:
            deletion = dp[j][i + 1] + 1
        elif i == len(seq1) - 1:
            insertion = dp[j + 1][i] + 1
        else:
            if seq1[i + 1] == seq2[j + 1]:
                substitution_or_pass = dp[j + 1][i + 1]
            else:
                substitution_or_pass = dp[j + 1][i + 1] + 1
                
            deletion = dp[j][i + 1] + 1
            insertion = dp[j + 1][i] + 1

        
        if j == len(seq2) - 1:
            dp[j][i] = deletion
        elif i == len(seq1) - 1:
            dp[j][i] = insertion
        else:
            dp[j][i] = min(substitution_or_pass, deletion, insertion)
                      
print(dp[0][0])                

f.close()

