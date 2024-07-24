from math import comb

name = input()
f = open(name, 'r')

n = int(f.readline()[:-1])
sum = 0

for i in range(n + 1):
    sum += comb(n, i)


print(sum % 1000000)

f.close()