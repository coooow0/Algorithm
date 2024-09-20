t = int(input())
for i in range(t):
    dp = [1, 0]
    n = int(input())
    if n == 0:
        print(dp[0], dp[1])
    else:
        for i in range(n):
            a, b = dp[1], sum(dp)
            dp = [a, b]
        print(a, b)