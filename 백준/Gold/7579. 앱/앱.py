import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

app = list(map(int, input().strip().split()))

c = list(map(int, input().strip().split()))
max_c = sum(c)

graph = [[0 for _ in range(max_c + 1)] for _ in range(n + 1)]

res = 10000001
for i in range(1, n + 1):
    for j in range(max_c + 1):
        a, v = app[i- 1], c[i - 1]
        
        if j - v >= 0:
            graph[i][j] = max(graph[i - 1][j], graph[i - 1][j - v] + a)
        else:
            graph[i][j] = graph[i-1][j]

        if graph[i][j] >= m:
            res = min(res, j)
print(res)
        