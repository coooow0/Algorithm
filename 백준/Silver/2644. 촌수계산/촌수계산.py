import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input().strip())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

x, y = map(int, input().strip().split())
# 둘의 사이를 알아내라

m = int(input().strip())

for _ in range(m):
    a, b = map(int,input().strip().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start, depth):
    if start == y:
        print(depth)
        return depth
    
    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            result = dfs(next, depth + 1)
        
            if result:
                return result

visited[x] = True
res = dfs(x, 0)

if not res:
    print(-1)