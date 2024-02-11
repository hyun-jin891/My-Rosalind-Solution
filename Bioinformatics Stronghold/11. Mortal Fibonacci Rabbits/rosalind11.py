n, m = map(int, input().split())

newRabbit = [0] * (n + 1)
newRabbit[1] = 1
totalRabbit = [0] * (n + 1)
totalRabbit[1] = 1

for i in range(2, n + 1):
    newRabbit[i] = totalRabbit[i - 1] - newRabbit[i - 1]    
    totalRabbit[i] = totalRabbit[i - 1] - newRabbit[i - m] + newRabbit[i]

print(totalRabbit[-1])



