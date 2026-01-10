from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())

queue = deque(list(map(int, input().strip().split())))

queue = deque([(queue[i - 1], i)for i in range(1, n + 1)])

res = []

for _ in range(n):
    a, b = queue.popleft()
    res.append(b)
    
    if a == 1:
        continue
    elif a > 0:
        queue.rotate(-(a - 1))
    else:
        queue.rotate(-a)
print(*res)