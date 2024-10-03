# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6) # 제귀 제한을 늘림
input = sys.stdin.readline

def DFS(v):
    global visited
    visited[v] = True
    for next in range(1, n+1):
        if not visited[next] and graph[v][next] : # 방문을 하지 않았을 경우
            DFS(next)

    
n, m = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)    

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        # 방문을 하지 않았다면
        DFS(i)
        cnt += 1
print(cnt)