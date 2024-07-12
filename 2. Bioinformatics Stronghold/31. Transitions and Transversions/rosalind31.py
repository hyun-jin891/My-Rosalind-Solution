

seq1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
seq2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"


current_index = 0
num_transition = 0
num_transversion = 0
base_dictionary = {"G" : "Purine", "A" : "Purine", "C" : "Pyrimidine", "T" : "Pyrimidine"}

while current_index < len(seq1):
    base_seq1 = seq1[current_index]
    base_seq2 = seq2[current_index]
    
    if base_seq1 == base_seq2:
        pass
    else:
        if base_dictionary[base_seq1] == base_dictionary[base_seq2]:
            num_transition += 1
        else:
            num_transversion += 1
    
    current_index += 1
    

print(num_transition/num_transversion)
    
    
    




