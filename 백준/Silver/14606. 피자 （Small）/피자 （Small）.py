n = int(input())
dp = [0] * (n + 1)
if n > 1:
    dp[2] = 1
    for i in range(3, n + 1):
        if i % 2 == 0: #even
            dp[i] = (i // 2) ** 2 + (2 * dp[i // 2])
        else:
            dp[i] = (i // 2 + 1) * (i // 2) + (dp[i // 2 + 1] + dp[i // 2])
print(dp[n])