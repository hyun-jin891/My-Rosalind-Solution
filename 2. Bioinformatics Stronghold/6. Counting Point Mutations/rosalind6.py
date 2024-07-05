file_name = input()

f = open(file_name, 'r')

seq1 = f.readline()
seq2 = f.readline()

count = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        count += 1

print(count)
f.close()