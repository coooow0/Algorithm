import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

cnt = dict()

for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

res = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        res[stack.pop()] = arr[i]
    
    stack.append(i)
print(*res)
