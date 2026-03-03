import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

rev_arr = arr[::-1]
res = [0 for _ in range(n)]
stack = []


for i in range(n):
    while stack and rev_arr[i] > arr[stack[-1]]:
        res[stack.pop()] = n - i
    stack.append(n - i - 1)
print(*res)