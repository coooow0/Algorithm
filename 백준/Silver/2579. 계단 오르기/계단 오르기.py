import sys
input = sys.stdin.readline

t = int(input()) # 테스트 개수
st = [0] * 301 # 계단 값 초기화
for i in range(t):
    st[i] = int(input())

dp = [0] * 301 # 계단 합 초기화

dp[0] = st[0] # 1층의 경우
dp[1] = st[0] + st[1] # 2층의 경우
dp[2] = max(st[0] + st[2], st[1] + st[2]) # 3층의 경우 (첫 값은 무조건 포함x, 마지막 값만 무조건 포함. )

for i in range(3, t):
    dp[i] = st[i] + max(dp[i - 3] + st[i - 1], dp[i - 2])
print(dp[t - 1])