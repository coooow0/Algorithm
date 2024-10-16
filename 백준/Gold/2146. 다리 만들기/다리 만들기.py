# 다리 만들기
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
maps = [list(map(int, input().strip().split())) for _ in range(n)]
island = 2 # 섬의 라벨링을 위해 초기화
ans = sys.maxsize

# 섬 구분하는 bfs
def bfs(row, col):
    queue = deque()
    queue.append([row, col])
    maps[row][col] = island
    while queue: # 큐가 빌 때 까지
        row, col = queue.popleft()
        for check_r, check_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = row + check_r
            nc = col + check_c
            if 0 <= nr < n and 0 <= nc < n: # 범위 이내고
                if maps[nr][nc] == 1: # 해당 위치가 1인 경우
                    maps[nr][nc] = island # 섬의 라벨을 붙여줌
                    queue.append([nr, nc])
    
def bfs_bridge(island_num): # 다리 길이를 재기 위함
    queue = deque()
    dist = [[-1] * n for _ in range(n)] # 최단 거리를 재단하기 위해 -1로 초기화를 함
    
    for i in range(n): # 
        for k in range(n):
            if maps[i][k] == island_num:
                queue.append([i, k])
                dist[i][k] = 0 # 주변에 1을 더해 길이를 잴 것이기 때문에 0으로 초기화
                
    while queue: 
        row, col = queue.popleft()
        for check_r, check_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = row + check_r
                nc = col + check_c
                if 0 <= nr < n and 0 <= nc < n:
                    if maps[nr][nc] == 0 and dist[nr][nc] == -1: # 바다이고, 방문한 적이 없는 경우
                        queue.append([nr, nc]) # 새로 방문한 바다 좌표를 추가
                        dist[nr][nc] = dist[row][col] + 1 # 지금까지 이동한 거리에서 1을 더함
                    elif maps[nr][nc] > 0 and maps[nr][nc] != island_num: # 다른 섬에 도달한 경우
                        return dist[row][col] # 현재까지의 거리 반환

for i in range(n): # row
    for k in range(n): # col
        if maps[i][k] == 1:
            bfs(i, k) # 열, 행
            island += 1 # 다른 섬임을 표시하기 위해 1을 더해줌

for i in range(2, island):
    ans = min(ans, bfs_bridge(i))

print(ans)