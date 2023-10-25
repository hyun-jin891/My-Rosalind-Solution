DNA_seq = input()
reverse_c = ""

for i in range(len(DNA_seq) - 1, -1, -1):
    symbol = DNA_seq[i]
    newSymbol = ''
    
    if symbol == 'A':
        newSymbol = 'T'
    elif symbol == 'T':
        newSymbol = 'A'
    elif symbol == 'G':
        newSymbol = 'C'
    elif symbol == 'C':
        newSymbol = 'G'
    reverse_c += newSymbol

print(reverse_c)