from collections import deque
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
arr = deque(arr)
rot = 0 # m명씩 제거됐을 떄 원 돌리기

direc = True

while arr:
    if direc:
        arr.rotate(-(k - 1))
    else:
        arr.rotate(k)
    
    print(arr.popleft())
    rot += 1
    
    if rot == m:
        rot = 0
        direc = not direc

            
            