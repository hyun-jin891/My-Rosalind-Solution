from math import log10

def base_count(seq):
    A_or_T_count = 0
    G_or_C_count = 0
    
    for i in range(len(seq)):
        if seq[i] == 'A' or seq[i] == 'T':
            A_or_T_count += 1
        else:
            G_or_C_count += 1
    
    return A_or_T_count, G_or_C_count

name = input()
f = open(name, 'r')
seq = ""
GC_contents = []

for line in f.readlines():
    if line[0] == '0':
        GC_contents = list(map(float, line.split()))
    else: 
        seq += line[:-1]


AT_count, GC_count = base_count(seq)


for i in range(len(GC_contents)):
    GC_content = GC_contents[i]
    A_or_T = (1 - GC_content) / 2
    G_or_C = GC_content / 2
    if i == len(GC_contents) - 1:
        print(log10(A_or_T ** AT_count) + log10(G_or_C ** GC_count))
    else:
        print(log10(A_or_T ** AT_count) + log10(G_or_C ** GC_count), end=' ')
    



f.close()

