import sys
input = sys.stdin.readline

t = int(input()) # 테스트 개수
st = [int(input()) for _ in range(t)] # 각 계단의 값을 저장

if t == 1:
    print(st[0])
elif t == 2:
    print(st[0] + st[1])
else:
    dp = [0] * t # 계단의 합을 더하기 위한 배열
    
    dp[0] = st[0] # 1층의 경우
    dp[1] = st[0] + st[1] # 2층의 경우
    dp[2] = max(st[0] + st[2], st[1] + st[2]) # 3층의 경우 (첫 값은 무조건 포함x, 마지막 값만 무조건 포함. )

    for i in range(3, t):
        dp[i] = st[i] + max(dp[i - 3] + st[i - 1], dp[i - 2])
    print(dp[t - 1])