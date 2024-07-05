def GC_Calculator(seq):
    length = len(seq)
    GC_count = 0
    
    for s in seq:
        if s == 'G' or s == 'C':
            GC_count += 1
    
    return (GC_count / length) * 100

name = input()
f = open(name, 'r')

max_ID = ""
max_value = 0
test = 0
last_seq = ""
last_ID = ""


for line in f.readlines():
    if test == 0:
        seq = ""
        ID = ""
        test += 1
        
    if line[0] == ">":
        if seq != "":
            value = GC_Calculator(seq)
            seq = ""
            if value > max_value:
                max_value = value
                max_ID = ID
        ID = line[1 : -1]
    else:
        seq += line[:-1]
    
    last_seq = seq
    last_ID = ID

last_value = GC_Calculator(last_seq)
if last_value > max_value:
    max_value = last_value    
    max_ID = last_ID
print(max_ID)
print(max_value)
f.close()