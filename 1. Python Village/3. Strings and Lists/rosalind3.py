name = input()
f = open(name, 'r')

NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string = ""

for line in f.readlines():
    if line[0] not in NUMBER:
        string += line[:-1]
    else:
        a, b, c, d = list(map(int, line[:-1].split()))



print(string[a : b + 1], string[c : d + 1])