n, k = map(int, input().split())

dp = [0] * (n + 1)


dp[1] = 1


for i in range(2, len(dp)):
    baby = dp[i - 2] * k
    dp[i] = dp[i - 1] + baby

print(dp[-1])
    