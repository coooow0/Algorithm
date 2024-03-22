from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

visited1 = [0] * (n+1)
visited2 = visited1.copy()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    # 이어진 간선을 만들기 위해 a, b 위치를 바꾸어서도 1로 만들어줌

def DFS(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(n+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            DFS(i)
            # 그래프에 1이 칠해져 있고, 방문하지 않은 노드일 때

def BFS(v):
    visited2[v] = 1
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(n+1):
            if graph[v][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

DFS(v)
print()
BFS(v)