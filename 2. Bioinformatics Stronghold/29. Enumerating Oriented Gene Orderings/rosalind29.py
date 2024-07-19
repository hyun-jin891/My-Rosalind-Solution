from itertools import permutations
from math import factorial

name = input()
f = open(name, 'r')
n = int(f.readline()[:-1])

print(2 ** n * factorial(n))

permutation_list = []

for i in range(2 ** n):
    numList = [0] * n
    for j in range(n):
        if i & (1<<j) != 0:
            numList[j] = -(j + 1)
        else:
            numList[j] = j + 1
            
    permutation_list.extend(list(permutations(numList)))
    
for i in range(len(permutation_list)):
    for j in range(len(permutation_list[i])):
        if j == len(permutation_list[i]) - 1:
            print(permutation_list[i][j])
        else:
            print(permutation_list[i][j], end = " ")    
        
            
f.close()      


