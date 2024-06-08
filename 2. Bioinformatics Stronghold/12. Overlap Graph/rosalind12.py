name = input()
file = open(name, 'r')
FASTA_name = []
seqs = []
flag = True


for line in file.readlines():
    if line[0] == '>':
        if flag == True:
            FASTA_name.append(line[1:-1])
            resultSeq = ""
            flag = False
        else:
            seqs.append(resultSeq)
            FASTA_name.append(line[1:-1])
            resultSeq = ""
    else:
        resultSeq += line[:-1]
        
seqs.append(resultSeq)

for i in range(len(FASTA_name)):
    suffix = seqs[i][-3] + seqs[i][-2] + seqs[i][-1]

    for j in range(len(FASTA_name)):
        if i == j:
            continue
        else:
            prefix = seqs[j][0:3]
            if suffix == prefix:
                print(FASTA_name[i], FASTA_name[j])
           
         




