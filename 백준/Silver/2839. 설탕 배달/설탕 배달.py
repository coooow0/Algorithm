import sys
input = sys.stdin.readline 

n = int(input())

dp = [5000] * (n + 1)

if n < 6:
    if n == 3 or n == 5:
        print(1)
        exit()
    else:
        print(-1)
        exit()
dp[3] = 1
dp[5] = 1

for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    
if dp[i] >= 5000:
    print(-1)
else:
    print(dp[n])