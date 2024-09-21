import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = a[:]
 # dp는 수열의 합을 계산함

for i in range(1, n):
    for k in range(i):
        if a[i] > a[k]:
            dp[i] = max(dp[k] + a[i], dp[i])
print(max(dp))