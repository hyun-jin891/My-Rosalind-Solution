matching_dic = {"" : 1, "A" : 1, "U" : 1, "G" : 1, "C" : 1, "AA" : 1, "AC" : 1, "AU" : 2, "AG" : 1, "CA" : 1, "CU" : 1, "CG" : 2, "CC" : 1, "UA" : 2, "UU" : 1, "UG" : 1, "UC" : 1, "GA" : 1, "GC" : 2, "GU" : 1, "GG" : 1}

def calculate_num(seq):
    if seq not in matching_dic:
        matching_dic[seq] = 0
        for i in range(1, len(seq)):
            if matching_dic[seq[0] + seq[i]] == 1:
                continue
            else:
                subseq1 = seq[1 : i]
                subseq2 = seq[i + 1:]

                res1 = calculate_num(subseq1)
                res2 = calculate_num(subseq2)

                matching_dic[seq] += (res1 * res2) % 1000000
        
        matching_dic[seq] += calculate_num(seq[1:])        

        
    return (matching_dic[seq]) % 1000000


seq = ""

name = input()
f = open(name, 'r')

f.readline()

for line in f.readlines():
    seq += line[:-1]

print((calculate_num(seq)) % 1000000)

f.close()