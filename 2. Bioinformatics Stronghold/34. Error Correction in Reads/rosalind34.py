base_pair = {'T' : 'A', 'A' : 'T', 'G' : 'C', 'C' : 'G'}

def reverse_complement(seq):
    res = ""
    for i in range(len(seq) - 1, -1, -1):
        base = seq[i]
        res += base_pair[base]
    
    return res

def calculate_hamming_dist(seq1, seq2):
    hamming_dist = 0
    reverse_hamming_dist = 0
    original_base_index = 0
    mutation_base_index = 0
    reverse_original_index = 0
    reverse_mutation_index = 0
    
    for i in range(len(seq1)):
        if hamming_dist >= 2 and reverse_hamming_dist >= 2:
            return None
        if seq1[i] != seq2[i]:
            hamming_dist += 1
            original_base_index = i
            mutation_base_index = i
        if base_pair[seq1[i]] != seq2[len(seq2) - i - 1]:
            reverse_hamming_dist += 1
            reverse_original_index = i
            reverse_mutation_index = len(seq2) - i - 1
    
    if hamming_dist == 1:
        seq2_list = list(seq2)
        seq2_list[mutation_base_index] = seq1[original_base_index]
        seq2 = ''.join(seq2_list)
    elif reverse_hamming_dist == 1:
        seq2_list = list(seq2)
        seq2_list[reverse_mutation_index] = base_pair[seq1[reverse_original_index]]
        seq2 = ''.join(seq2_list)

    
    return seq2




reads = []
read_dictionary = {}
name = input()
f = open(name, 'r')

f.readline()
temp_read = ""

for line in f.readlines():
    if line[0] == '>':
        reads.append(temp_read)
        temp_read = ""
    else:
        temp_read += line[:-1]

reads.append(temp_read)

for i in range(len(reads)):
    read = reads[i]
    
    if read not in read_dictionary.keys():
        reverseComplement = reverse_complement(read)
        if reverseComplement in read_dictionary.keys():
            read_dictionary[reverseComplement] += 1
        else:
            read_dictionary[read] = 1
    else:
        read_dictionary[read] += 1

correct_reads = []
incorrect_reads = []

for key, value in read_dictionary.items():
    if value >= 2:
        correct_reads.append(key)
    else:
        incorrect_reads.append(key)

for i in range(len(incorrect_reads)):
    res = incorrect_reads[i] + "->"
    for j in range(len(correct_reads)):
        new_seq2 = calculate_hamming_dist(correct_reads[j], incorrect_reads[i])
        if new_seq2 == None:
            continue
        else:
            res += new_seq2
    
    print(res)
        

        