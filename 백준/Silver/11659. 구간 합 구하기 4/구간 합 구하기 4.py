import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
sum_arr = [0]
total = 0

for a in arr:
    total += a
    sum_arr.append(total)

for _ in range(m):
    i, j = map(int, input().strip().split())
    print(sum_arr[j] - sum_arr[i-1])