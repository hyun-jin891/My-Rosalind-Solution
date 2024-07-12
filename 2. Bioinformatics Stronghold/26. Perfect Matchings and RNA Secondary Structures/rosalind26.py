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

dp = [0] * (max(AU_pair, GC_pair) + 1)
dp[1] = 1

for i in range(2, len(dp)):
    dp[i] = dp[i - 1] * i

print(dp[AU_pair//2] * dp[GC_pair//2])