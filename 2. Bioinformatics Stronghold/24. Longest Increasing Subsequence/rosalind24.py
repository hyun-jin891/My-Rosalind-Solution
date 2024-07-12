
name = input()
f = open(name, 'r')

n = int(f.readline())
l = list(map(int, f.readline().split()))

increased_l = sorted(l)
decreased_l = sorted(l, reverse=True)

l = [0] + l
increased_l = [0] + increased_l
decreased_l = [0] + decreased_l

dp_increase = [[0 for i in range(len(l) + 1)] for i in range(len(l) + 1)]
dp_decrease = [[0 for i in range(len(l) + 1)] for i in range(len(l) + 1)]

for i in range(1, len(increased_l)):
    for j in range(1, len(l)):
        if increased_l[i] == l[j]:
            dp_increase[i][j] = dp_increase[i - 1][j - 1] + 1
        else:
            dp_increase[i][j] = max(dp_increase[i - 1][j], dp_increase[i][j - 1])

increased_res = ""

current_i = len(increased_l) - 1
current_j = len(l) - 1

while current_i >= 1 and current_j >= 1:
    if dp_increase[current_i][current_j] == dp_increase[current_i - 1][current_j]:
        current_i = current_i - 1
        continue
    elif dp_increase[current_i][current_j] == dp_increase[current_i][current_j - 1]:
        current_j = current_j - 1
        continue
    else:
        increased_res = str(l[current_j]) + " " + increased_res
        current_i = current_i - 1
        current_j = current_j - 1
        

for i in range(1, len(decreased_l)):
    for j in range(1, len(l)):
        if decreased_l[i] == l[j]:
            dp_decrease[i][j] = dp_decrease[i - 1][j - 1] + 1
        else:
            dp_decrease[i][j] = max(dp_decrease[i - 1][j], dp_decrease[i][j - 1])

decreased_res = ""

current_i = len(decreased_l) - 1
current_j = len(l) - 1

while current_i >= 1 and current_j >= 1:
    if dp_decrease[current_i][current_j] == dp_decrease[current_i - 1][current_j]:
        current_i = current_i - 1
        continue
    elif dp_decrease[current_i][current_j] == dp_decrease[current_i][current_j - 1]:
        current_j = current_j - 1
        continue
    else:
        decreased_res = str(l[current_j]) + " " + decreased_res
        current_i = current_i - 1
        current_j = current_j - 1     

        
print(increased_res)
print(decreased_res)       
        
    
    

    