def calculate_prob_motif(motif, GC_content):
    AT_content = 1 - GC_content
    G_prob = GC_content / 2
    C_prob = GC_content / 2
    A_prob = AT_content / 2
    T_prob = AT_content / 2
    
    base_prob = {'A' : A_prob, 'T' : T_prob, 'G' : G_prob, 'C' : C_prob}
    res = 1
    
    for i in range(len(motif)):
        res *= base_prob[motif[i]]
    
    return res


name = input()
f = open(name, 'r')
N, x = list(map(float, f.readline().split()))
seq = ""

for line in f.readlines():
    seq += line[:-1]

prob_motif = calculate_prob_motif(seq, x)

print(1 - (1 - prob_motif) ** N)




f.close()

