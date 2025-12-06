from collections import deque

import sys
input = sys.stdin.readline

a, k = map(int, input().split())

#BFS로 풀기. 큐에 넣은 값이랑 깊이를 넣장

visited = [False for _ in range(1000001)]


def bfs():
    queue = deque()
    queue.append((a, 0))
    
    while queue:
        num, depth = queue.popleft()
        if num == k:
            print(depth)
            break
        
        for next in [num + 1, num * 2]:
            if next <= 1000000 and not visited[next]:
                visited[next] = True
                queue.append((next, depth + 1))
                
bfs()