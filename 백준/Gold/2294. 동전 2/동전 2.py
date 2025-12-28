import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr = set(arr)
arr = list(arr)
arr.sort(reverse=True)

dp = [100000] * (100001)

for i in arr:
    dp[i] = 0
    
for i in range(1, k + 1):
    for num in arr:
        if i != num and i >= num:
            dp[i] = min(dp[i], dp[i - num])
    dp[i] += 1
    

print(-1 if dp[k] >= 100000 else dp[k])