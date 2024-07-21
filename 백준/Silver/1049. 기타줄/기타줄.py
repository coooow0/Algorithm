import math
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0, 0] for _ in range(m)]
for i in range(m):
    arr[i][0], arr[i][1] = map(int, input().split())

arr.sort(key=lambda x : x[0])
pack = arr[0][0] * math.ceil(n/6) #패키지로 샀을 때
ans = arr[0][0] * int(n/6)

arr.sort(key=lambda x :x[1])
one = arr[0][1] * n
ans += arr[0][1] * (n%6)

print(min(pack, one, ans))
