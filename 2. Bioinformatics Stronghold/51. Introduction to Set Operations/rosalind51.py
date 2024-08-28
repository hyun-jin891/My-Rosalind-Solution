name = input()
f = open(name, 'r')

n = int(f.readline()[:-1])

totalSet = set(range(1, n + 1))

iter_A = ""
iter_B = ""
flagA = True

for line in f.readlines():
    if flagA:
        if line[-2] == '}':
            iter_A += line[:-1]
            flagA = False
        else:
            iter_A += line[:-1]
    else:
        iter_B += line[:-1]

setA = set()

temp = ""
for i in range(len(iter_A)):
    if iter_A[i] == '{' or iter_A[i] == '}' or iter_A[i] == ',' or iter_A[i] == ' ':
        if temp == "":
            continue
        setA.add(int(temp))
        temp = ""
        continue
    else:
        temp += iter_A[i]

setB = set()

temp = ""
for i in range(len(iter_B)):
    if iter_B[i] == '{' or iter_B[i] == '}' or iter_B[i] == ',' or iter_B[i] == ' ':
        if temp == "":
            continue
        setB.add(int(temp))
        temp = ""
        continue
    else:
        temp += iter_B[i]

f.close()

print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
print(totalSet.difference(setA))
print(totalSet.difference(setB))