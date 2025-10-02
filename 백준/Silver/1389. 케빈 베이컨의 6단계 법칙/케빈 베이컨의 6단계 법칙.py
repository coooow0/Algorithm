# 케빈 베이컨의 6단계 법칙
from collections import deque

import sys
input = sys.stdin.readline

queue = deque()
            
def bfs(start):
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    cnt = 0
    queue.append((start, cnt))
    
    while queue:    
        num, level = queue.popleft()
        result[start][num] = level
        for x in graph[num]:
            if not visited[x]: # 방문하지 않았을 경우
                queue.append((x, level+1))
                visited[x] = True


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 여유분을 더 만듦
result = [[0 for _ in range(n + 1)] for _ in range(n+1)] # 케빈 베이컨 수를 저장함

for _ in range(m):
    r, c = map(int, input().split())
    graph[r].append(c)
    graph[c].append(r)

for i in range(1, n+1):
    bfs(i)
    
arr = [sum(result[i]) for i in range(1, n+1)]
print(arr.index(min(arr)) + 1)
