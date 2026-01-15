import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().strip().split())

graph = [[]for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False for _ in range(n + 1)]
visited_bfs = [False for _ in range(n + 1)]

arr_dfs = []
arr_bfs = []
def dfs(start):
    for next in graph[start]:
        if not visited_dfs[next]:
            visited_dfs[next] = True
            arr_dfs.append(next)
            dfs(next)
    
    

visited_dfs[v] = True
arr_dfs.append(v)
dfs(v)

def bfs():
    while queue:
        start = queue.popleft()
        arr_bfs.append(start)
        
        for next in graph[start]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                queue.append(next)

visited_bfs[v] = True
queue = deque()
queue.append(v)

bfs()

print(*arr_dfs)
print(*arr_bfs)
