import sys
input = sys.stdin.readline

n = int(input())

DP = [0 for _ in range(n+1)]

if n == 1 or n == 2:
    print(1)
else:
    DP[1] = 1
    DP[2] = 1
    for i in range(3, n+1):
        DP[i] = DP[i-2] + DP[i-1]
    print(DP[i])
