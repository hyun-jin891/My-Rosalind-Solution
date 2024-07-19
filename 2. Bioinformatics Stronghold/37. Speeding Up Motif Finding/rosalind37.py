

seq = ""

name = input()
f = open(name, 'r')
f.readline()

for line in f.readlines():
    seq += line[:-1]

failure_array = [0] * len(seq)

i = 0

for j in range(1, len(seq)):
    while i > 0 and seq[i] != seq[j]:
        i = failure_array[i - 1]
    
    if seq[i] == seq[j]:
        i += 1
        failure_array[j] = i
    

for i in range(len(failure_array)):
    print(failure_array[i], end = " ")

f.close()