def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


name = input()
f = open(name, "r")

n = f.readline()
n = int(n)

count = 0
numList = list(range(1, n + 1))

permutation = factorial(n)

res = ["" for i in range(permutation)]

    
tryNum = 0
preElementNumber = 0

while tryNum < n:
    tryNum += 1

    elementNumber = factorial(n - (tryNum - 1)) / (n - tryNum + 1)
    alreadyInvolveNum = []
    temp = 0
    for i in range(len(res)):
        if preElementNumber != 0 and i % preElementNumber == 0:
            alreadyInvolveNum = []
        else:
            if i % elementNumber != 0:
                temp = 0
            elif i != 0:
                alreadyInvolveNum.append(temp)
        for j in range(len(numList)):      
            candidateNum = numList[j]
            if candidateNum in alreadyInvolveNum:
                continue
            if str(candidateNum) not in res[i]:
                res[i] += str(candidateNum) + " "
                temp = candidateNum
                break
    preElementNumber = elementNumber

print(permutation)
for i in range(len(res)):
    print(res[i])

f.close()