# DFS와 BFS
import sys
def DFS(idx):
    global visited
    visited[idx] = True # 방문 처리
    print(idx, end=' ')
    for next in range(1, n+1):
        if not visited[next] and graph[next][idx]:
            # 방문을 하지 않았고, 그래프에 위치가 True일 경우
            DFS(next)

def BFS():
     global q, visited
     while q:
         cur = q.pop(0)
         print(cur, end = ' ')
         for next in range(1, n+1):
             if not visited[next] and graph[cur][next]:
                 visited[next] = True
                 q.append(next)
                 

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m): # 간선의 개수
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = True, True
    # 정점을 있다고 표시함
    
DFS(v)
print()

visited = [False] * (n+1)
q = [v] 
visited[v] = True # 이미 방문 처리를 함
BFS()


