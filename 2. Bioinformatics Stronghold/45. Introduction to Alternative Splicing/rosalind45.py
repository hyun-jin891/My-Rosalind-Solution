from math import comb


name = input()
f = open(name, 'r')

n, m = list(map(int, f.readline().split()))

res = 0

for i in range(m, n + 1):
    res += comb(n, i) % 1000000


print(res % 1000000)

f.close()



