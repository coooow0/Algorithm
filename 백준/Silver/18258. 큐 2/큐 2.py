#  큐 2
from collections import deque
import sys
input = sys.stdin.readline

arr = deque()

n = int(input().strip())
for _ in range(n):
    command = list(input().strip().split(' '))
    if command[0] == 'push':
        arr.append(int(command[1]))
        
    elif command[0] == 'pop':
        print(arr.popleft() if len(arr) != 0 else -1)
    
    elif command[0] == 'size':
        print(len(arr))
        
    elif command[0] == 'empty':
        print(1 if len(arr) == 0 else 0)
        
    elif command[0] == 'front':
        print(arr[0] if len(arr) != 0 else -1)
    
    else:
        print(arr[-1] if len(arr) != 0 else -1 )