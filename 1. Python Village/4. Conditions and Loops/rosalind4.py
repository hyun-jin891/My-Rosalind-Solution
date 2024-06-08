name = input()
f = open(name, 'r')

a, b = list(map(int, f.readline().split()))
sum = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        sum += i

print(sum)