name = input()
f = open(name, 'r')
prob = [1, 1, 1, 0.75, 0.5, 0]

line = f.readline()
population = line.split()
sum = 0

for i in range(len(prob)):
    sum += int(population[i]) * prob[i]

print(2 * sum)

