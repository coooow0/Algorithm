# 카드 구매하기
import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1): # i장의 카드를 뽑을 때 최대값
    for k in range(1, i+1): # 카드팩 P[k]의 값..
        dp[i] = max(dp[i], dp[i-k] + p[k])
        # 최대값을 더하다보면 전의 값에서 + 하는 것을 볼 수 있음. 
print(dp[-1])
