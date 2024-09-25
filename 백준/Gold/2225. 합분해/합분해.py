# 합분해
# 0부터 n까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수

n, k = map(int, input().split()) # 열, 행

dp = [[0 for _ in range(n + 1)] for _ in range(k+1)]
# 합을 저장함. 넉넉히 잡았음
for i in range(k+1):
    dp[i][0] = 1

for i in range(1, k + 1): # 행 
    for j in range(1, n + 1): # 열
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 
print(dp[k][n] % 1000000000)
