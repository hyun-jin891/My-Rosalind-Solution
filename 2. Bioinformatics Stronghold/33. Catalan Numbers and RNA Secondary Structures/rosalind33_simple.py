matching_dic = {"" : 1, "AA" : 0, "AC" : 0, "AU" : 1, "AG" : 0, "CA" : 0, "CU" : 0, "CG" : 1, "CC" : 0, "UA" : 1, "UU" : 0, "UG" : 0, "UC" : 0, "GA" : 0, "GC" : 1, "GU" : 0, "GG" : 0}
def calculate_catalan(seq):
    if seq not in matching_dic:
        matching_dic[seq] = 0
        for i in range(1, len(seq), 2):
            matching_dic[seq] += matching_dic[seq[0] + seq[i]] * calculate_catalan(seq[1:i]) * calculate_catalan(seq[i + 1:]) 
    
    return matching_dic[seq] % 1000000        

seq = ""
dp = [{} for i in range(len(seq) // 2)]
name = input()
f = open(name, 'r')

f.readline()

for line in f.readlines():
    seq += line[:-1]
    
print(calculate_catalan(seq))

f.close()