from collections import deque

import sys
input = sys.stdin.readline

n = int(input().strip()) # 동기의 수
graph = [[]for _ in range(n + 1)]

m = int(input().strip()) # 간선
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

    
arr = graph[1]
# 1이랑 연결된 애들이 있음

visited = [False for _ in range(n + 1)]
visited[1] = True
cnt = 0

for i in graph[1]:
    visited[i] = True

for i in graph[1]:
    for k in graph[i]:
        if not visited[k]:
            visited[k] = True

for i in visited:
    if i == True:
        cnt += 1
print(cnt - 1)
