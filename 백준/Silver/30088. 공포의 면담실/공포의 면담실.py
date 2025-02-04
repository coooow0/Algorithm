import sys
input = sys.stdin.readline
n = int(input())
# arr = list(map(int, input().split()))
res = [0]

for _ in range(n):
    arr = list(map(int, input().split()))
    res.append(sum(arr[1:]))
res.sort()

for i in range(1, n+1):
    res[i] += res[i-1]
print(sum(res))