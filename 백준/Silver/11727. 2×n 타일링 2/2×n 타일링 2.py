import sys
input = sys.stdin.readline

n = int(input())
DP = [ 0 for _ in range(10001)]

DP[1] = 1
DP[2] = 3
for i in range(3, n + 1):    
    DP[i] = DP[i-1] + 2 * DP[i-2]

print(DP[n] % 10007)
