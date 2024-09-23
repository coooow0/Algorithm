# 연속합
# 임의의 수열에서 연속된 몇 개의 수를 선택해 구할 수 있는 합 중 가장 큰 합을 구하려고 함
# 10
# 2 1 -4 3 4 -4 6 5 -5 1 -> 3 4 -4 6 5 로 14가 답이 됨

n = int(input())
a = list(map(int, input().split()))

dp = list(a[i] for i in range(n)) # 수열의 합을 저장한다. 

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])
print(max(dp))