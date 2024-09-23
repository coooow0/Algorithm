import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for k in range(i):
        if a[i] < a[k]:
            dp[i] = max(dp[k] + 1, dp[i])
print(max(dp))