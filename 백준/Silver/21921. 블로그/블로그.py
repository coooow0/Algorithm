import sys
input = sys.stdin.readline

n, x = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

dp = [0 for _ in range(n + 1)]

dp[1] = arr[0]

for i in range(2, n + 1):
    dp[i] = dp[i-1] + arr[i-1]

visited = 0

for i in range(1, n + 1):
    visited = max(visited, dp[i]-dp[i-x])
    
if visited == 0:
    print('SAD')
    exit()
    
print(visited)

cnt = 0
for i in range(1, n + 1):
    if visited == dp[i] - dp[i-x]:
       cnt += 1 
print(cnt)