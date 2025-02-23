# 카드 1
from collections import deque
n = int(input())
arr = [i for i in range(1, n + 1)]
arr = deque(arr)

while True:
    if len(arr) == 1:
        print(arr.popleft())
        break
    print(arr.popleft(), end=' ')
    arr.append(arr.popleft())
    