# 수들의 합 5
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0 # 가지수를 세는 변수

for i in range(1, n + 1):
    res = 0
    for k in range(i, n + 1):
        res += k
        if res == n:
            cnt += 1
        elif res > n:
            break
print(cnt)