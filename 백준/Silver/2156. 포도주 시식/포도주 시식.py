import sys
input = sys.stdin.readline

t = int(input())

g = [0] * 10000 # 포도주 양 초기화 glass
for i in range(t):
    g[i] = int(input()) # 포도주 양 입력받음


dp = [0] * 10000

dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(dp[1], g[0] + g[2], g[1] + g[2])

for i in range(3, t):
    dp[i] = max(g[i] + g[i-1] + dp[i-3], g[i] + dp[i-2], dp[i-1])
    # 1. 현재, 이 전 마시고 전전은 안 마실 경우. dp[i-2]는 전전을 포함한 것
    # 2. 현재, 이 전은 마시지 않을 경우
    # 3. 현재 마시지 않음
print(dp[t-1])