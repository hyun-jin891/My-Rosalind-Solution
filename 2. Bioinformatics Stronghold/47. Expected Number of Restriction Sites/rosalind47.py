


name = input()
f = open(name, 'r')

N = int(f.readline()[:-1])
flag = True
seq = ""
GC_content_line = ""

for line in f.readlines():
    if line[0] == "0":
        if flag:
            GC_content_line += line[:-1]
            flag = False
        else:
            GC_content_line += " "
            GC_content_line += line[:-1]
    else:
        seq += line[:-1]

GC_content_line = list(map(float, GC_content_line.split()))

for i in range(len(GC_content_line)):
    current_GC = GC_content_line[i]
    current_AT = 1 - current_GC
    
    G_prob = current_GC/2
    C_prob = current_GC/2
    A_prob = current_AT/2
    T_prob = current_AT/2
    
    base_prob = {'G' : G_prob, 'C' : C_prob, 'T' : T_prob, 'A' : A_prob}
    res = N - len(seq) + 1
    
    for j in range(len(seq)):
        res *= base_prob[seq[j]]
    
    print(res, end=" ")


f.close()