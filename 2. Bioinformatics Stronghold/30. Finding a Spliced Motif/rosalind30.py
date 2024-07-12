
name = input()
f = open(name, 'r')

seq1 = ""
seq2 = ""
flag = False

f. readline()

for line in f.readlines():
    if line[0] == '>':
        flag = True
        
    else:
        if flag:
            seq2 += line[:-1]
        else:
            seq1 += line[:-1]
        

res = [0] * len(seq2)

symbol_seq2_index = 0

for i in range(len(seq1)):
    if seq1[i] == seq2[symbol_seq2_index]:
        res[symbol_seq2_index] = i + 1
        symbol_seq2_index += 1
    if symbol_seq2_index == len(seq2):
        break

for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i])
    else:
        print(res[i], end=" ")