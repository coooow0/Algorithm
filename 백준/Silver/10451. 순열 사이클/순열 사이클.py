# 순열 사이클
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)
    


tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = [0]
    arr += list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i in range(1, n+1):
        graph[i].append(arr[i])
        
    answer = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    print(answer)