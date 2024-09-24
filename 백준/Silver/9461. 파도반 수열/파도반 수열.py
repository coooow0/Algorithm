# 파도반 수열
import sys
input = sys.stdin.readline

n = int(input())
a = [0] * (101)

for i in range(1, n+1):
    a[i] = int(input())
    dp = [0] * (101) # 수열의 합

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for k in range(4, a[i] + 1):
        dp[k] = dp[k - 3] + dp[k - 2]
    print(dp[a[i]])

