import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n, k = map(int, input().strip().split())

graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
# m행 n열

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().strip().split())
    
    for i in range(y1, y2): # 행
        for j in range(x1, x2): # 열
            if not graph[i][j]:
                graph[i][j] = 1

def dfs(r, c):
    graph[r][c] = 1
    count = 1
    
    for dr, dc in dir:
        new_r, new_c = r + dr, c + dc
        if 0<= new_r < m and 0<= new_c <n and not graph[new_r][new_c]:
                count = count + dfs(new_r, new_c)
    return count

    
    
res = 0
cnt = []
for i in range(m):
    for k in range(n):
        if graph[i][k] == 0:
            res += 1
            graph[i][k] = 1
            cnt.append(dfs(i, k))
cnt.sort()
print(res)
print(*cnt)