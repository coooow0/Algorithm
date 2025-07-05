from collections import deque
import sys

input = sys.stdin.readline
queue = deque() 

def bfs():
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in d:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < n and 0 <= new_c < m:
                # 범위 내이고
                if graph[new_r][new_c] == 1 and visited[new_r][new_c] == -1:
                    visited[new_r][new_c] = visited[row][col] + 1
                    queue.append((new_r, new_c))
                
    for i in range(n):
        for k in range(m):
            if graph[i][k] == 0:
                visited[i][k] = 0
    
    
                    

n, m = map(int, input().strip().split())

graph = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().strip().split())))
    if 2 in graph[i]:
        idx = graph[i].index(2)
        queue.append((i, idx))
        visited[i][idx] = 0
        
# 각 지점부터 목표 지점까지의 거리

bfs()
for i in visited:
    print(*i)