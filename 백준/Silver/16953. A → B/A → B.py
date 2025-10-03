from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
queue = deque()

def bfs():
    while queue:
        num, cnt = queue.popleft()
        
        if num == b:
            print(cnt+1)
            return
        
        for next in [num * 2, int(str(num) + '1')]:
            if next <= b:
                queue.append((next, cnt + 1))
            
    return print(-1)

queue.append((a, 0))
# 메모리 초과로 인해 큐에 현재 연산 횟수도 넣음
bfs()
