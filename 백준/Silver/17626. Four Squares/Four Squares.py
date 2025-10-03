import sys
input = sys.stdin.readline

n = int(input())

dp =[0 for _ in range(n+1)]

for i in range(1, n + 1):
    min_v = 50001
    
    for k in range(1, int(i ** 0.5) + 1):
        min_v = min(dp[i - k * k] + 1, min_v)
    dp[i] = min_v
    
print(dp[n])