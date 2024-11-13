# 퇴사
import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n + 1)
day = []
for i in range(n):
    t, p = map(int, input().strip().split())
    day.append([t, p])

for i in range(n):
    t, p = day[i]  # i번째 날의 상담 기간과 수익을 가져옴
    if i + t <= n:  # 현재 상담이 퇴사일을 넘지 않는다면
        dp[i + t] = max(dp[i + t], dp[i] + p)  # 상담이 끝난 날의 최대 수익 갱신
    dp[i + 1] = max(dp[i + 1], dp[i])  # 다음 날로 이익을 이어감

print(dp[n])