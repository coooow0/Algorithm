import sys
input = sys.stdin.readline

t = int(input())
n = list(map(int, input().split()))
dp = [1] * t # 수열의 길이를 구하기 위한 배열

# 10
# 10 20 10 30 20 50 11 12 13 14 15  이 경우를 생각하기.

for i in range(1, t): # 기준이 되는 수
    for k in range(i): # 비교되는 수
        if n[i] > n[k] and dp[i] <= dp[k]:
            # 기준 숫자보다 작은데, 수열의 길이가 같거나 긴 경우
            # == 떨거지(?) 숫자들이 있는 경우 나한테 붙임
            dp[i] = dp[k] + 1
print(max(dp))