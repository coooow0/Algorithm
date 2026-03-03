import sys
input = sys.stdin.readline

n = int(input().strip())

arr = [int(input().strip()) for _ in range(n)]
stack = []
cnt = 0

for i in range(n):
    while stack and arr[i] >= stack[-1]:
        stack.pop()
    
    cnt += len(stack)
    stack.append(arr[i])

print(cnt)