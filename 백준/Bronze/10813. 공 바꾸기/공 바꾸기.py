import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = i

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

for i in range(1, n+1):
    print(arr[i], end=" ")