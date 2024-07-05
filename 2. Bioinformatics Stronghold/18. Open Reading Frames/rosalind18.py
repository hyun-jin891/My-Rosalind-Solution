import re

codonTable = {"TTT" : "F", "TTC" : "F", "TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "ATT" : "I", "ATC" : "I", "ATA" : "I", "ATG" : "M", "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V", "TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "TAT" : "Y", "TAC" : "Y", "CAT" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "AAT" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "GAT" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "TGT" : "C", "TGC" : "C", "TGG" : "W", "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGT" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}

def otherStrand(seq):
    resSeq = ""
    for i in range(len(seq)):
        base = seq[i]
        if base == "A":
            resSeq += "T"
        elif base == "T":
            resSeq += "A"
        elif base == "G":
            resSeq += "C"
        else:
            resSeq += "G"
    
    return resSeq

def Translate(seq, start_index):
    resProtein = ""
    currentIndex = start_index
    flag = False
    
    while (currentIndex <= len(seq) - 3):
        current_codon = seq[currentIndex : currentIndex + 3]
        if current_codon not in codonTable.keys():
            flag = True
            break
        amino_acid = codonTable[current_codon]
        resProtein += amino_acid
        currentIndex += 3
    
    if (flag):
        return resProtein
    else:
        return ""
    

name = input()
f = open(name, 'r')

Seq = ""
f.readline()

for line in f.readlines():
    Seq += line[:-1]


reExpForStart = "(?=" + "ATG" + ")"


compilerForStart = re.compile(reExpForStart)


Seq_Starts = compilerForStart.finditer(Seq)


startCodonIndex = []


for i in Seq_Starts:
    startCodonIndex.append(i.span()[0])




res = []


for i in range(len(startCodonIndex)):
    start_index = startCodonIndex[i]
    proteinSeq = Translate(Seq, start_index)
    if (proteinSeq == ""):
        continue
    else:
        res.append(proteinSeq)


Seq = otherStrand(Seq)    
reverseSeq = Seq[-1 : : -1]
Seq_Starts = compilerForStart.finditer(reverseSeq)

startCodonIndex = []

for i in Seq_Starts:
    startCodonIndex.append(i.span()[0])

for i in range(len(startCodonIndex)):
    start_index = startCodonIndex[i]
    proteinSeq = Translate(reverseSeq, start_index)
    if (proteinSeq == ""):
        continue
    else:
        res.append(proteinSeq)

res = set(res)
for seq in res:
    print(seq)

f.close()