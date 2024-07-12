from math import perm

name = input()
f = open(name, 'r')

n, k = list(map(int, f.readline().split()))

print(perm(n, k) % 1000000)