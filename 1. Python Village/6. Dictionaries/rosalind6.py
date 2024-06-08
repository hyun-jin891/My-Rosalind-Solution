name = input()
f = open(name, 'r')
string = ""
res = {}

for line in f.readlines():
    string += line[:-1]

word_list = string.split()

for i in range(len(word_list)):
    word = word_list[i]
    if word not in res:
        res[word] = 1
    else:
        res[word] += 1

for k, v in res.items():
    print(k, v)