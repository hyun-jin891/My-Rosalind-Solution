import re

file_name = input()
f = open(file_name, 'r')

Seq = f.readline()[:-1]
Motifs = "(?=" + f.readline()[-1] + ")"



compiled = re.compile(Motifs)


it = compiled.finditer(Seq)

for i in it:
    print(i.span()[0] + 1, end= " ")

f.close()