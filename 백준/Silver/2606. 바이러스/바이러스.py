# 바이러스 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# 1번 컴퓨터가 바이러스에 걸렸을 경우, 바이러스에 걸리는 컴퓨터의 수를 출력

n = int(input().strip())
m = int(input().strip()) # 연결되어있는 간선의 개수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    row, col = map(int, input().split())
    graph[row].append(col)
    graph[col].append(row)
visited = [False] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(visited.count(True) - 1) # 1번도 포함하기 때문에