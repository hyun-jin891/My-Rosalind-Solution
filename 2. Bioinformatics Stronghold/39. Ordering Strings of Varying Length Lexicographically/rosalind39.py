from itertools import combinations_with_replacement
from itertools import permutations

def compareStr(str1, str2, characters_dict):
    maxStr = ""
    minStr = ""
    if len(str1) >= len(str2):
        maxStr = str1
        minStr = str2
    else:
        maxStr = str2
        minStr = str1
    
    for i in range(len(maxStr)):
        if i >= len(minStr):
            return minStr, maxStr
        elif characters_dict[maxStr[i]] > characters_dict[minStr[i]]:
            return minStr, maxStr
        elif characters_dict[maxStr[i]] < characters_dict[minStr[i]]:
            return maxStr, minStr

    return minStr, maxStr
            
            
    

def quick_sort(iter, character_dict):
    if len(iter) == 1 or len(iter) == 0:
        return iter

    pivot = (0 + len(iter) - 1) // 2
    back = []
    forward = []
    
    for i in range(len(iter)):
        if i == pivot:
            continue
        back_str, for_str = compareStr(iter[i], iter[pivot], character_dict)

        if back_str == iter[pivot]:
            forward.append(for_str)
        elif for_str == iter[pivot]:
            back.append(back_str)

    return quick_sort(back, character_dict) + [iter[pivot]] + quick_sort(forward, character_dict)
            
    



char_dict = {}

name = input()
f = open(name, 'r')

characters = f.readline().split()

for i in range(len(characters)):
    char_dict[characters[i]] = i

n = int(f.readline()[:-1])

comb = []

for i in range(1, n + 1):
    temp = list(combinations_with_replacement(characters, i))
    for j in range(len(temp)):
        comb.extend(list(permutations(temp[j])))

for i in range(len(comb)):
    comb[i] = "".join(comb[i])

comb = list(set(comb))

new_comb = quick_sort(comb, char_dict)

for i in range(len(new_comb)):
    print(new_comb[i])

f.close()





