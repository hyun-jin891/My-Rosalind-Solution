from math import comb
from math import factorial

base_dict = {'A' : 0, 'U' : 0, 'G' : 0, 'C' : 0}

seq = ""

name = input()
f = open(name, 'r')
f.readline()

for line in f.readlines():
    seq += line[:-1]

for i in range(len(seq)):
    base_dict[seq[i]] += 1

res = 1

count_A = base_dict['A']
count_U = base_dict['U']
count_G = base_dict['G']
count_C = base_dict['C']

if count_A >= count_U:
    res *= comb(count_A, count_U) * factorial(count_U)
else:
    res *= comb(count_U, count_A) * factorial(count_A)

if count_G >= count_C:
    res *= comb(count_G, count_C) * factorial(count_C)
else:
    res *= comb(count_C, count_G) * factorial(count_G)

print(res)

f.close()

