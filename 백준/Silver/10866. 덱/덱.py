from collections import deque
import sys

n = int(sys.stdin.readline())
arr = deque()
for i in range(n):
    inner = list(sys.stdin.readline().strip().split())
    if inner[0] == 'push_front':
        arr.appendleft(inner[1])

    elif inner[0] == 'push_back':
        arr.append(inner[1])

    else:
        if inner[0] == 'pop_front':
            if arr:
                print(arr[0])
                arr.popleft()
            else:
                print(-1)

        elif inner[0] == 'pop_back':
            if arr:
                print(arr[-1])
                arr.pop()

            else:
                print(-1)

        elif inner[0] == 'size':
            print(len(arr))
        
        elif inner[0] == 'empty':
            if arr:
                print(0)
            else :
                print(1)
            
        elif inner[0] == 'front':
            if arr:
                print(arr[0])
            else:
                print(-1)
        
        else:
            if arr:
                print(arr[-1])
            else:
                print(-1)