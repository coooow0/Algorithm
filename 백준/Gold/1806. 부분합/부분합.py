# 부분합
import sys
input = sys.stdin.readline

n, s = [*map(int, input().split())]
arr = [*map(int, input().split())]

ans = n + 1 # 정답 개수를 세는 변수
start = 0
res = 0

for end in range(n):
    res += arr[end]
    
    while res >= s:
        res -= arr[start]
        ans = min(ans, end - start + 1) # 최소 길이 갱신
        start += 1


print(ans if ans != n + 1 else 0)