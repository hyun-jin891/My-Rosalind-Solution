DNA_seq = input()
RNA_seq = ""

for i in range(len(DNA_seq)):
    symbol = DNA_seq[i]
    
    if symbol == 'T':
        RNA_seq += 'U'
    else:
        RNA_seq += symbol

print(RNA_seq)