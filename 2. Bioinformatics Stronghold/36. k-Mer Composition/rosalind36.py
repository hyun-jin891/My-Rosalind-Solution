from itertools import product

seq = ""

name = input()
f = open(name, 'r')
f.readline()

for line in f.readlines():
    seq += line[:-1]

base = ['A', 'T', 'G', 'C']
k_mer_candidates = list(product(base, repeat=4))
new_k_mer_c = [0] * len(k_mer_candidates)

for i in range(len(k_mer_candidates)):
    new_k_mer_c[i] = ''.join(k_mer_candidates[i])

v = [0] * len(k_mer_candidates)
k_mer_dict = dict(zip(new_k_mer_c, v))


for i in range(len(seq) - 3):
    k_mer = seq[i : i + 4]
    
    if k_mer in k_mer_dict.keys():
        k_mer_dict[k_mer] += 1

k_mer_key = list(k_mer_dict.keys())
k_mer_key.sort()

for i in range(len(k_mer_key)):
    print(k_mer_dict[k_mer_key[i]], end=" ")


f.close()














