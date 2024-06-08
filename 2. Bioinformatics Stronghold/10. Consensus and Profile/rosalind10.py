nucleotides = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
reverse_nt = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
def create_profile_consensus(seqs):
    res1 = [[0 for i in range(len(seqs[0]))] for i in range(4)]
    res2 = ""
    
    for i in range(len(seqs[0])):
        for j in range(len(seqs)):           
            nt_index = nucleotides[seqs[j][i]]
            res1[nt_index][i] += 1
    for i in range(len(seqs[0])):
        max_symbol = reverse_nt[0]
        max_freq = res1[0][i]
        for j in range(4):
            if max_freq < res1[j][i]:
                max_symbol = reverse_nt[j]
                max_freq = res1[j][i]
        res2 += max_symbol
            
    
    return res1, res2
        

file_name = input()
f = open(file_name, 'r')


Seqs = []
res = ""
for line in f.readlines():
    if line[0] == ">":
        if res != "":
            Seqs.append(res)
            res = ""
        continue
    else:
        res += line[:-1]

Seqs.append(res)

profile, consensus = create_profile_consensus(Seqs)

print(consensus)

for i in range(len(profile)):
    print(reverse_nt[i] + ":", end="")
    for j in range(len(profile[i])):
        print(" " + str(profile[i][j]), end="")
    print()


