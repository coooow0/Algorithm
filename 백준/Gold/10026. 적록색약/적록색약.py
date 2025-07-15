# 적록색약 
# 초록이랑 빨간색 구분을 못함.. 
import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(arr):
    while queue:
        row, col = queue.popleft()
        for dr, dc in d:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < n and 0 <= new_c < n :
                if graph[row][col] == graph[new_r][new_c] and not arr[new_r][new_c]:
                    # 나의 값과 같고, 방문하지 않았을 경우 
                    queue.append((new_r, new_c))
                    arr[new_r][new_c] = True
    
n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

cnt = 0

for i in range(n):
    for k in range(n):
        if not visited[i][k]: # 방문하지 않았을 경우
            queue.append((i, k))
            visited[i][k] = True
            bfs(visited)
            cnt += 1
            
print(cnt, end=' ')
visited_color = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for k in range(n):
        if graph[i][k] == 'G':
            graph[i][k] = 'R'

not_color = 0

for i in range(n):
    for k in range(n):
        if not visited_color[i][k]:
            queue.append((i, k))
            visited_color[i][k] = True
            bfs(visited_color)
            not_color += 1
print(not_color)