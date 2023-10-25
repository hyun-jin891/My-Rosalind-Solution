d = {}

seqs = input()

for i in range(len(seqs)):
    symbol = seqs[i]
    if symbol not in d:
        d[symbol] = 1
    else:
        d[symbol] += 1

d = sorted(d.items())

for k, v in d:
    print(v, end=' ')