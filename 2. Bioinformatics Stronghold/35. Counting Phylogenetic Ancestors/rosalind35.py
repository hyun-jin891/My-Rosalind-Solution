name = input()
f = open(name, 'r')

n = int(f.readline())

print(n - 2)

f.close()