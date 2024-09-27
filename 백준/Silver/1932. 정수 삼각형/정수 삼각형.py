# 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i]=(list(map(int, input().split())))
    dp[i].append(0)
if n > 1:    
    dp[1][0] += dp[0][0]
    dp[1][1] += dp[0][0]
        
    for i in range(2, n):
        dp[i][0] += dp[i-1][0]
        for j in range(1, i+1):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1])) 