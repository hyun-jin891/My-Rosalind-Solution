from collections import deque

def BFS_seq_graph(seq1, seq2):
    need_v = deque()
    visited = dict()
    first_edit_num = 0
    need_v.append((len(seq1) - 1, len(seq2) - 1, first_edit_num))
    visited[(len(seq1) - 1, len(seq2) - 1)] = first_edit_num
    
    while need_v:
        current_x, current_y, current_edit_n = need_v.popleft()
        
        
        #print(current_x, current_y, current_edit_n)
        
        #print(current_x, current_y)
        
        if current_y <= 0 or current_x <= 0:
            continue
        
        #if current_x == 0 and current_y == 1:
        #    return current_edit_n
        
        
        #if (current_x, current_y) in visited:
         
         #   continue
        
        if seq1[current_x] == seq2[current_y]:
            if (0, 1) in visited.keys():
                if visited[(0, 1)] <= current_edit_n:
                    continue
            if (current_x - 1, current_y - 1) in visited.keys():
                if current_edit_n >= visited[(current_x - 1, current_y - 1)]:
                    continue
                      
            need_v.append((current_x - 1, current_y - 1, current_edit_n))
            visited[(current_x - 1, current_y - 1)] = current_edit_n
                
        else:
            direction = [(1, 1), (1, 0), (0, 1)]
            if (0, 1) in visited.keys():
                if visited[(0, 1)] <= current_edit_n +1:
                    continue
            
            for i in range(len(direction)):
                next_x = current_x - direction[i][0]
                next_y = current_y - direction[i][1]
                
                if (next_x, next_y) in visited.keys():
                    if current_edit_n + 1 >= visited[(next_x, next_y)]:
                        continue
                need_v.append((next_x, next_y, current_edit_n + 1))
                visited[(next_x, next_y)] = current_edit_n + 1
    
    return visited[(0, 1)]   
        
seq1 = ""
seq2 = ""

name = input()
f = open(name, 'r')

f.readline()
flag = False

for line in f.readlines():
    if line[0] == '>':
        flag = True
        continue
    if flag:
        seq2 += line[:-1]
    else:
        seq1 += line[:-1]
          
seq1 = "0" + seq1
seq2 = "0" + seq2
print(BFS_seq_graph(seq1, seq2))

f.close()


