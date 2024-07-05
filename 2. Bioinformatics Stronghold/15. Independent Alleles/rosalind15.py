def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def combination(n, r):
    return factorial(n)/(factorial(r) * factorial(n - r))

name = input()
f = open(name, 'r')
k, N = list(map(int, f.readline().split()))

prob = 1
num = 2 ** k

for i in range(N):
    sub_prob = combination(num, i) * (0.75 ** (num - i)) * (0.25 ** i)
    prob -= sub_prob

print(prob)

f.close()