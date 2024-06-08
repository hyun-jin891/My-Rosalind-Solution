name = input()
f = open(name, 'r')
a, b = list(map(int, f.readline().split()))

print(a ** 2 + b ** 2)