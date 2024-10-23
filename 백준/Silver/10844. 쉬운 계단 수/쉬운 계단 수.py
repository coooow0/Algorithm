n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1
dp[0][1] = 1
for i in range(2, n + 1):
    for k in range(1, 10):
        if k == 1:
            dp[i][1] = dp[i - 2][1] + dp[i - 1][2]

        elif k == 9:
            dp[i][9] = dp[i - 1][8]

        else:
            dp[i][k] = dp[i - 1][k - 1] + dp[i - 1][k + 1]
            
print(sum(dp[n]) % 1000000000)