import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
arr.sort()

result = 0
for i in range(n):
    result = max(result, arr[i] * (n - i))
print(result)