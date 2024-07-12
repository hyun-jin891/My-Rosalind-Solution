base_pair = {'U' : 'A', 'A' : 'U', 'G' : 'C', 'C' : 'G'}
def calculate_catalan(dp, seq, start, end):
    if end - start == 1 or end - start == -len(seq) + 1:
        if seq[start] == base_pair[seq[end]]:
            dp[1][start + 1] = 1
        else:
            dp[1][start + 1] = 0
        return
    
    first_base = seq[start]
    temp_1 = 0
    temp_2 = 0
    temp_res = 0
    
    n = end - start + 1
    if end - start < 0:
        n = end - start + len(seq) + 1

    
    for i in range(1, n, 2):
        index = start + i
        if start + i >= len(seq):
            index = index - len(seq)
        m_base = seq[index]
        if m_base == base_pair[first_base]:
            if i == 1:
                dp[1][start + 1] = 1
                temp_1 = 1
            else:
                temp_index = start + 1
                if start + 1 >= len(seq):
                    temp_index = 0
                
                temp_index2 = start + i - 1
                if start + i - 1 >= len(seq):
                    temp_index2 = temp_index2 - len(seq)
                temp_total_size = temp_index2 - temp_index + 1
            
                if temp_index2 - temp_index < 0:
                    temp_total_size = temp_index2 - temp_index + len(seq) + 1
                
                if temp_total_size == 2:
                    if seq[temp_index2] == base_pair[seq[temp_index]]:
                        temp_1 = 1
                    else:
                        temp_1 = 0
                else:
            
                    if dp[temp_total_size // 2][temp_index + 1] != -1:
                        temp_1 += dp[temp_total_size // 2][temp_index + 1]
                    else:
                        calculate_catalan(dp, seq, temp_index, temp_index2)
                        temp_1 += dp[temp_total_size // 2][temp_index + 1]

            if i == n - 1:
                if i + start >= len(seq):
                    dp[1][i + start - len(seq) + 1] = 1
                else:
                    dp[1][start + i + 1] = 1
                temp_2 = 1
            else:
                temp_index = start - 1
                if start - 1 <= 0:
                    temp_index = len(seq) - 1
                if start < end and (temp_index > end or temp_index < start):
                    temp_index = end
                elif start > end and (end < temp_index < start):
                    temp_index = end
                    
                temp_index2 = start + i + 1
                if start + i + 1 >= len(seq):
                    temp_index2 = temp_index2 - len(seq)
                


                temp_total_size = temp_index - temp_index2 + 1
                if temp_index - temp_index2 < 0:
                    temp_total_size = temp_index - temp_index2 + len(seq) + 1
                
                if temp_total_size == 2:
                    if seq[temp_index2] == base_pair[seq[temp_index]]:
                        temp_2 = 1
                    else:
                        temp_2 = 0
                else:
            
                    if dp[temp_total_size // 2][temp_index2 + 1] != -1:
                        temp_2 += dp[temp_total_size // 2][temp_index2 + 1]
                    else:
                        calculate_catalan(dp, seq, temp_index2, temp_index)
                        temp_2 += dp[temp_total_size // 2][temp_index2 + 1]
            

            temp_res += temp_1 * temp_2
            temp_1 = 0
            temp_2 = 0

    
    dp[n // 2][start + 1] = temp_res % 1000000
            

seq = ""
dp = [{} for i in range(len(seq) // 2)]
name = input()
f = open(name, 'r')

f.readline()

for line in f.readlines():
    seq += line[:-1]
    
dp = [[-1 for i in range(len(seq) + 1)] for i in range(len(seq) // 2 + 1)]
dp[0] = [1 for i in range(len(seq) + 1)]

calculate_catalan(dp, seq, 0, len(seq) - 1)

print(dp[-1][1])

