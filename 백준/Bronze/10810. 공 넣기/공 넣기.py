import sys
n, m = map(int, input().split())
arr = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for a in range(i, j+1):
        arr[a] = k

for a in range(1, n+1):
    print(arr[a], end=" ")