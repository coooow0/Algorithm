import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for i in range(n + 1)]
dp[1] = [1] * 10
for i in range(n + 1):
    dp[i][1] = 1

for i in range(2, n+1):
    for k in range(10):
        dp[i][k] = dp[i-1][k] + dp[i][k-1]

print(sum(dp[n]) % 10007)