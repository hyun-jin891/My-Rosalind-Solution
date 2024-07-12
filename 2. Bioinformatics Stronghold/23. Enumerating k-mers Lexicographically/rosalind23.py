from itertools import product

name = input()
f = open(name, 'r')

alphabet = f.readline().split()
n = int(f.readline())
string = ""

for i in product(alphabet, repeat=n):
    for k in list(i):
        string += k
    print(string)
    string = ""


