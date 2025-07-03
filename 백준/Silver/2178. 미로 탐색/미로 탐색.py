from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    while queue:
        row, col = queue.popleft()
        # [0, 0]
        for nr, nc in d:
            new_r = row+nr
            new_c = col+nc
            
            if 0 <= new_r < n and 0<= new_c <m:
                if graph[new_r][new_c] == 1 and not visited[new_r][new_c]:
                    # 통행할 수 있고, 방문하지 않았을 경우
                    graph[new_r][new_c] = graph[row][col] + 1
                    visited[new_r][new_c] = True
                    queue.append((new_r, new_c))
    print(graph[n-1][m-1])
n, m = map(int, input().strip().split())
graph = []


for _ in range(n):
    graph.append(list(map(int,input().strip())))
    
visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
# 맨 처음 (1, 1)은 무조건 1인셈.. 큐에 넣어주기
bfs()
