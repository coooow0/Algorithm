import sys
input = sys.stdin.readline

n = int(input().strip())

arr = [ list(map(int, input().strip().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1], x[0]))
cnt = 1
tmp = arr[0][1]
for i in range(1, n):
    if arr[i][0] >= tmp:
        cnt += 1
        tmp = arr[i][1]
print(cnt)