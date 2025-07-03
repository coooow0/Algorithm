from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    
    while queue:
        floors, row, col = queue.popleft()
        # 층, 행, 열 넣어줌
        for nf, nr, nc in d:
            new_f, new_r, new_c = nf + floors, nr + row, nc + col
            if 0 <= new_f < l and 0 <= new_r <r and 0<= new_c <c:
                # 범위 내에 있으면 
                if (arr[new_f][new_r][new_c] == '.' or arr[new_f][new_r][new_c] == 'E')and visited[new_f][new_r][new_c] == 0:
                    # 방문 안 했으면 
                        visited[new_f][new_r][new_c] = visited[floors][row][col] + 1
                        queue.append((new_f, new_r,new_c))
                        
while True:
    l, r, c = map(int, input().strip().split())
    if l == 0:
        break
    
    arr = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    
    
    for i in range(l): #층
        for j in range(r): #행
            arr[i][j] = list(input().strip())
            if 'S' in arr[i][j]:
                a = arr[i][j].index('S')
                visited[i][j][a] = 1
            # 입력 받으면서 S 자리 탐색할수도 있음         
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    # 사람이 있을 경우
                    # visited[i][j][k] = 1
                    bfs(i, j, k) # 주변 탐색을 위해.. 
                    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'E':
                    if visited[i][j][k] == 0:
                        print("Trapped!")
                        
                    else:
                        print("Escaped in " + str(visited[i][j][k] - 1) + " minute(s).")
