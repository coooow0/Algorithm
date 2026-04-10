import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

arr = []

for _ in range(n):
    b = list(map(int, input().strip().split()))
    arr.append(b)

graph = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

res = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        w, v = map(int, arr[i - 1])
        
        if j - w >= 0:
            graph[i][j] = max(graph[i- 1][j], graph[i - 1][j - w] + v)
        else:
            graph[i][j] = graph[i - 1][j]
print(graph[n][k])