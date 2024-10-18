# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input().strip())

def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
            arr[i] = n
            
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
arr = [0] * (n + 1)
for _ in range(n-1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    dfs(i)

for i in range(2, n+1):
    print(arr[i])