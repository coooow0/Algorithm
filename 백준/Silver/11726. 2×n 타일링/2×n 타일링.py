n = int(input())
DP = [ 0 for _ in range(10001)]

DP[1] = 1
DP[2] = 2
for i in range(3, n + 1):    
    DP[i] = DP[i-1] + DP[i-2]

print(DP[n] % 10007)
