import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

cnt = 0

for i in arr:
    if i > n:
        cnt += n
    else:
        cnt += i

print(cnt)