# 알파벳 개수

s = list(input())

a = ord('a') - 97
z = ord('z') - 97

dp = [0] * (z - a + 1)

for i in range(len(s)):
    for k in range(a, z + 1):
        if ord(s[i]) == k + 97:
            dp[k] += 1

for i in dp:
    print(i, end=' ')