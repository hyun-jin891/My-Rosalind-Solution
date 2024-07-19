def overlap_reads(seq1, seq2):
    if len(seq1) <= len(seq2):
        minSeq = seq1
        maxSeq = seq2
    else:
        minSeq = seq2
        maxSeq = seq1
    for i in range(len(minSeq)):
        if minSeq[i:] == maxSeq[: len(minSeq) - i]:
            return len(minSeq) - i, (minSeq, 0, i), maxSeq
    for i in range(len(minSeq), -1, -1):
        if minSeq[:i] == maxSeq[len(maxSeq) - i : ]:
            return i, maxSeq, (minSeq, i, len(minSeq))
    
    return None, None, None
            
name = input()
f = open(name, 'r')
reads = []
f.readline()
seq = ""

for line in f.readlines():
    if line[0] == '>':
        reads.append(seq)
        seq = ""
        continue
    else:
        seq += line[:-1]

reads.append(seq)
seq = ""


while len(reads) > 1:
    maxLength = 0
    maxLeftSeqInfo = None
    maxRightSeqInfo = None
    res = ""
    remove_seq1 = ""
    remove_seq2 = ""
    
    for i in range(len(reads)):
        for j in range(i + 1, len(reads)):
            if i == j:
                continue
            else:
                seq1 = reads[i]
                seq2 = reads[j]
                
                overlap_length, leftSeqInfo, rightSeqInfo = overlap_reads(seq1, seq2)
                
                
                if overlap_length == None:
                    continue
                
                if overlap_length > maxLength:
                    maxLength = overlap_length
                    maxLeftSeqInfo = leftSeqInfo
                    maxRightSeqInfo = rightSeqInfo
                    remove_seq1 = seq1
                    remove_seq2 = seq2
                    

    if isinstance(maxLeftSeqInfo, tuple):
        res += maxLeftSeqInfo[0][maxLeftSeqInfo[1] : maxLeftSeqInfo[2]]
        res += maxRightSeqInfo
    else:
        res += maxLeftSeqInfo
        res += maxRightSeqInfo[0][maxRightSeqInfo[1] : maxRightSeqInfo[2]]
    
    reads.remove(remove_seq1)
    reads.remove(remove_seq2)
    reads.append(res)
                

print(reads[0])

                
f.close()
        
    
                
                
            