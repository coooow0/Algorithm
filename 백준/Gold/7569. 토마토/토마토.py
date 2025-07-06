from collections import deque
queue = deque()

import sys
input = sys.stdin.readline

d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def bfs():
    while queue:
        floor, row, col, cnt = queue.popleft()
        for nf, nr, nc in d:
            new_f, new_r, new_c = floor + nf, row + nr, col + nc
            if 0 <= new_f < h and 0 <= new_r < n and 0 <= new_c < m: # 범위 내이고
                if graph[new_f][new_r][new_c] == 0 and not visited[new_f][new_r][new_c]:
                    visited[new_f][new_r][new_c] = 1
                    queue.append((new_f, new_r, new_c, cnt + 1))
        
    return cnt

m, n, h = map(int, input().strip().split())

graph = [[list(map(int, input().strip().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1: # 토마토가 있으면 주변에 물들여야 하니까 큐에 저장
                visited[i][j][k] = 1
                queue.append((i, j, k, 0))
                # 현재 위치와 날짜를 입력함
            elif graph[i][j][k] == -1:
                visited[i][j][k] = 1
                # 애초에 방문하지 못하는 곳이니까 미리 1로 처리함
                  
if len(queue) == 0: # 맨 처음부터 토마토가 없을 경우
    print(-1)
    exit()
    
elif len(queue) == m * n * h:
    # 길이와 값이 같으면,, 이미 모든 토마토가 익어있는 상태임
    print(0)
    
else:
    days = bfs()
    for i in range(h):
        for j in range(n):
            if 0 in visited[i][j]:
                print(-1)
                exit()
    
    print(days)