n = int(input())
dp = [0] * (100001)
dp[1], dp[2], dp[3] = -1, 1, -1
dp[4], dp[5], dp[6] = 2, 1, 3
dp[7], dp[8] = 2, 4
for i in range(9, n + 1):
    dp[i] = dp[i - 5] + 1
print(dp[n])