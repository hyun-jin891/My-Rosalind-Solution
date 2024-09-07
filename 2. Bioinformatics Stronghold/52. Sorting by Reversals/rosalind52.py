from collections import deque

def convertToInversionSeq(seqL):
    res = [0] * (len(seqL)-2)
    res = [0] + res + [11]
    
    for i in range(1, len(seqL) - 1):
        res[i] = seqL.index(i)
    
    return res

def productByInversion(iseqL, seqL1):
    res = [0] * (len(seqL1)-2)
    res = [0] + res + [11]
    
    for i in range(1, len(iseqL) - 1):
        res[i] = iseqL[seqL1[i]]
    
    return res

def calculate_breakpoint(seq):
    breakpoints = []
    
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i - 1]) != 1:
            breakpoints.append(i)
    
    return breakpoints

def calculate_reversal_distance_with_collections(seq):
    need_v = deque()
    visited = set()
    need_v.append((seq, 0, []))
    visited.add(tuple(seq))
    
    while need_v:
        current_seq, current_inversion_count, current_rev_collections = need_v.popleft()

        if current_seq == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return current_inversion_count, current_rev_collections
        
        current_breakpoints = calculate_breakpoint(current_seq)
        
        min_breakpoint_count = len(current_breakpoints)
        next_seqs = []
        
        for i in range(len(current_breakpoints)):
            for j in range(i + 1, len(current_breakpoints)):
                next_seq = current_seq[:current_breakpoints[i]] + current_seq[current_breakpoints[i]:current_breakpoints[j]][::-1] + current_seq[current_breakpoints[j]:]
                
                if tuple(next_seq) in visited:
                    continue
                next_breakpoint_count = len(calculate_breakpoint(next_seq))
                
                if next_breakpoint_count < min_breakpoint_count:
                    min_breakpoint_count = next_breakpoint_count
                    next_seqs = [(next_seq, current_breakpoints[i], current_breakpoints[j] - 1)]
                elif next_breakpoint_count == min_breakpoint_count:
                    next_seqs.append((next_seq, current_breakpoints[i], current_breakpoints[j] - 1))
        
        for i in range(len(next_seqs)):
            need_v.append((next_seqs[i][0], current_inversion_count + 1, current_rev_collections + [(next_seqs[i][1], next_seqs[i][2])]))
            visited.add(tuple(next_seqs[i][0]))           
                
        
         
name = input()
f = open(name, 'r')

seq1 = [0] + list(map(int, f.readline()[:-1].split())) + [11]
seq2 = [0] + list(map(int, f.readline()[:-1].split())) + [11]

seq2 = convertToInversionSeq(seq2)
final_seq = productByInversion(seq2, seq1)
dist, rev_collections = calculate_reversal_distance_with_collections(final_seq)

print(dist)

for i in range(len(rev_collections)):
    print(rev_collections[i][0], rev_collections[i][1])

f.close()