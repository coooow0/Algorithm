k = int(input())

dp = [[0, 0] for _ in range(k + 1)]
dp[1] = [0, 1]

if k >=2:
    dp[2] = [1, 1]
    for i in range(3, k + 1):
        dp[i] = [dp[i-2][0]+ dp[i-1][0], dp[i-2][1] + dp[i-1][1]]
print(str(dp[k]).replace('[', '').replace(']', '').replace(',', ''))