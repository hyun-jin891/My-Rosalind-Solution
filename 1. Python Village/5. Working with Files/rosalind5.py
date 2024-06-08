name = input()
f = open(name, 'r')
count = 1

for line in f.readlines():
    if count % 2 == 0:
        print(line[:-1])
    count += 1
    
    