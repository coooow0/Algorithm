
import sys
input = sys.stdin.readline


n = int(input().strip())
arr = list(map(int, input().strip().split()))

cnt = 1

a = arr[0] % 2

for i in range(1, n):
    if a != arr[i] % 2:
        cnt += 1
        a = arr[i] % 2
print(cnt)