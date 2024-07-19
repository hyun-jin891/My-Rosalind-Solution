from collections import deque

def calculate_breakpoint(seq1, seq2):
    breakpoints = []
    
    for i in range(len(seq2) - 1):

        if seq1.index(seq2[i + 1]) - seq1.index(seq2[i]) != 1:
            breakpoints.append(i + 1)

    return breakpoints
    

def inversion_dist(seq1, seq2):
    seq1 = ['-'] + seq1
    seq2 = ['-'] + seq2
    visited_seq = set()
    need_v = deque()
    current_bps = calculate_breakpoint(seq1, seq2)

    need_v.append((seq2, 0, len(current_bps)))
    visited_seq.add(tuple(seq2))
    min_bp = 100

    
    while need_v:
        
        current_seq2, current_count, current_bp = need_v.popleft()
        print(current_seq2)
        #if min_bp < current_bp:
         #   continue
        
        current_bps = calculate_breakpoint(seq1, current_seq2)
        
        if current_seq2 == seq1:
            return current_count
            
        
        next_seq2 = []
        next_seqs = []
        min_bp = current_bp
        
        for i in range(len(current_bps) - 1):
            for j in range(i + 1, len(current_bps)):
                next_seq2 = current_seq2[:current_bps[i]] + current_seq2[current_bps[i]:current_bps[j] + 1][::-1] + current_seq2[current_bps[j] + 1:]
                next_bp = len(calculate_breakpoint(seq1, next_seq2))
                
                if tuple(next_seq2) in visited_seq:
                    continue
                
                if next_bp < min_bp:
                    min_bp = next_bp
                    next_seqs = []
                    next_seqs.append(next_seq2)
                elif next_bp == min_bp:
                    next_seqs.append(next_seq2)

        for i in range(len(next_seqs)):
            need_v.append((next_seqs[i], current_count + 1, min_bp))
            visited_seq.add(tuple(next_seqs[i]))          
                    


name = input()
f = open(name, 'r')

seq1 = []
seq2 = []

pairs = []

turn = 1

for line in f.readlines():
    if line[0] == '\n':
        pairs.append([seq1, seq2])

    else:
        if turn % 2 == 1:
            seq1 = list(map(int, line[:-1].split()))
            turn += 1
        else:
            seq2 = list(map(int, line[:-1].split()))
            turn += 1




for i in range(len(pairs)):
    permutation1 = pairs[i][0]
    permutation2 = pairs[i][1]

    print(inversion_dist(permutation1, permutation2), end = " ")

