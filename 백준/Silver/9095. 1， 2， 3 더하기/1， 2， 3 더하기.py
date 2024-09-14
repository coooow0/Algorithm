import sys
input = sys.stdin.readline

t = int(input())
DP = [ 0 for _ in range(12)]

DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(t):
    n = int(input())
    if n in [1, 2, 3]:
        print(DP[n])
        continue
        
    for k in range(4, n+1):
        DP[k] = DP[k-3] + DP[k-2] + DP[k-1]
    print(DP[n])