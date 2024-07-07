import re
codonTable = {"TTT" : "F", "TTC" : "F", "TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "ATT" : "I", "ATC" : "I", "ATA" : "I", "ATG" : "M", "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V", "TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "TAT" : "Y", "TAC" : "Y", "CAT" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "AAT" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "GAT" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "TGT" : "C", "TGC" : "C", "TGG" : "W", "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGT" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}

def translate(seq):
    startCodon = "(?=" + "ATG" + ")"
    compiler = re.compile(startCodon)
    startCodonLocations = compiler.finditer(seq)
    startCodonList = []

    
    for i in startCodonLocations:
        startCodonList.append(i.span()[0])

    protein = ""
    flag = False
    for i in range(len(startCodonList)):
        if (flag):
            break
        for j in range(startCodonList[i], len(seq), 3):
            codon = seq[j : j + 3]
            if codon not in codonTable.keys():
                flag = True
                break
            else:
                protein += codonTable[codon]
    return protein

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = len(array) // 2
    front_arr, pivot_arr, rear_arr = [], [], []

    for value in array:
        if value.getX() < array[pivot].getX():
            front_arr.append(value)
        elif value.getX() > array[pivot].getX():
            rear_arr.append(value)
        else:
            pivot_arr.append(value)
    if len(front_arr) == 0 and len(rear_arr) == 0 and len(pivot_arr) != 0:
        return pivot_arr
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(rear_arr)

name = input()
f = open(name, 'r')
f.readline()
count = 0
seq = ""
reExp = []
input_intron = ""

for line in f.readlines():
    if line[0] != '>':
        if count == 0:
            seq += line[:-1]
        else:
            input_intron += line[:-1]
            
    else:
        if count == 0:
            count += 1
        else:
            reExp.append(input_intron)
            input_intron = ""
            
reExp.append(input_intron)
 
        
candidate_seqs = []
ori_intron_location = []
overlap_intron_location = []

class Intron:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__pair = []
    
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getPair(self):
        return self.__pair
    def appendPair(self, other):
        self.__pair.append(other)
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

for i in range(len(reExp)):
    oneReExp = reExp[i]
    compiler = re.compile(oneReExp)
    introns = compiler.finditer(seq)
    
    for intron in introns:
        x = intron.span()[0]
        y = intron.span()[1]

        newIntron = Intron(x, y)
        ori_intron_location.append(newIntron)

for i in range(len(reExp)):
    oneReExp = "(?=" + reExp[i] + ")"
    compiler2 = re.compile(oneReExp)
    introns = compiler2.finditer(seq)
    
    for intron in introns:
        x = intron.span()[0]
        y = x + len(reExp[i])
        

        if Intron(x, y) in ori_intron_location:
            continue
        else:
            newIntron = Intron(x, y)
            overlap_intron_location.append(newIntron)

removedOriIntron = []
for i in range(len(ori_intron_location)):
    ori_intron1 = ori_intron_location[i]
    for j in range(i, len(ori_intron_location)):
        if i == j:
            continue
        else:
            ori_intron2 = ori_intron_location[j]
            if (ori_intron2.getX() >= ori_intron1.getX() and ori_intron2.getX() <= ori_intron1.getY() - 1) or (ori_intron2.getY() >= ori_intron1.getX() and ori_intron2.getY() <= ori_intron1.getY() - 1):
                removedOriIntron.append(ori_intron2)
                overlap_intron_location.append(ori_intron2)
                
new_ori_intron_location = []               
for i in range(len(ori_intron_location)):
    if ori_intron_location[i] not in removedOriIntron:
        new_ori_intron_location.append(ori_intron_location[i])
        


for i in range(len(overlap_intron_location)):
    overlap_intron = overlap_intron_location[i]
    for j in range(len(new_ori_intron_location)):
        new_ori_intron = new_ori_intron_location[j]
        
        if (overlap_intron.getX() >= new_ori_intron.getX() and overlap_intron.getX() <= new_ori_intron.getY() - 1) or (overlap_intron.getY() >= new_ori_intron.getX() and overlap_intron.getY() <= new_ori_intron.getY() - 1):
            overlap_intron.appendPair(new_ori_intron)
               
                        
for i in range(2 ** len(overlap_intron_location)):
    possibleSeq = ""
    removed_intron = []
    pre_ori_intron = -1
    for j in range(len(overlap_intron_location)):
        if i & (1 << j) != 0:
            for k in range(len(overlap_intron_location[j].getPair())):
                removed_intron.append(overlap_intron_location[j].getPair()[k])
        else:
            removed_intron.append(overlap_intron_location[j])
                
    new_ori_intron_location = new_ori_intron_location + overlap_intron_location
    new_ori_intron_location = quick_sort(new_ori_intron_location)          

    for l in range(len(new_ori_intron_location)):
        if new_ori_intron_location[l] in removed_intron:
            continue
        else:
            if pre_ori_intron != -1:
                possibleSeq += seq[pre_ori_intron : new_ori_intron_location[l].getX()]


            else:
                possibleSeq += seq[: new_ori_intron_location[l].getX()]


            pre_ori_intron = new_ori_intron_location[l].getY()

    possibleSeq += seq[pre_ori_intron :]

    candidate_seqs.append(possibleSeq)



proteins = []
for i in range(len(candidate_seqs)):
    proteins.append(translate(candidate_seqs[i]))

for i in range(len(proteins)):
    print(proteins[i])

f.close()