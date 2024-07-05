def preProcessingBCR(pattern):
    res = {}
    nucleotides = ["A", "G", "C", "T"]
    
    for nt in nucleotides:
        res[nt] = -1
    for i in range(len(pattern)):
        res[pattern[i]] = i
    
    return res

def preProcessingGCR(pattern):
    bpos = [0] * (len(pattern) + 1)
    shift = [0] * (len(pattern) + 1)
    
    i = len(pattern)
    j = len(pattern) + 1
    bpos[i] = j
    
    while i > 0:
        while j <= len(pattern) and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
            
        
        i -= 1
        j -= 1
        bpos[i] = j
        
    
    i = bpos[0]
    for j in range(len(pattern)):
        if shift[j] == 0:
            shift[j] = i
        if j == i:
            i = bpos[j]
    
    return shift        


def search(seq, pattern):
    BCR_dictionary = preProcessingBCR(pattern)
    GCR_shift = preProcessingGCR(pattern)
    
    i = 0
    res = []
    
    while i <= len(seq) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == seq[i + j]:
            j -= 1
        
        if j < 0:
            res.append(i)
            i += GCR_shift[0]
        else:
            i += max(GCR_shift[j + 1], j - BCR_dictionary[seq[i + j]])
    
    return res

file_name = input()
f = open(file_name, 'r')
Seq = f.readline()
Motifs = f.readline()



res_index = search(Seq[:-1], Motifs[:-1])

for i in res_index:
    print(i + 1, end=" ")

f.close()
    
    
    
    
    
    