res = []


def complement(base):
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "G":
        return "C"
    else:
        return "G"


def isPalindrome(seq):
    for i in range(len(seq) // 2):
        if seq[i] != complement(seq[len(seq) - 1 - i]):
            return False
    
    return True
    
def reversePalindrome(seq):
    for i in range(4, 13, 2):
        for j in range(len(seq) - i + 1):
            subseq = seq[j : j + i]
            if (isPalindrome(subseq)):
                res.append((j, len(subseq)))
                

name = input()
f = open(name, 'r')

DNA_seq = ""
f.readline()

for line in f.readlines():
    DNA_seq += line[:-1]


reversePalindrome(DNA_seq)

for p, l in res:
    print(p + 1, l)

f.close()