import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
alpha = [False for _ in range(27)]

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(r):
    graph.append(list(map(str, input().strip())))
    for k in graph[i]:
        alpha[ord(k) - 65] = True
        # 있는 상태임

ans = 0

def dfs(row, col, depth):
    global ans
    ans = max(ans, depth)
    
    for nr, nc in dir:
        new_r, new_c = nr + row, nc + col
        
        if 0 <= new_r < r and 0 <= new_c < c:
            target = graph[new_r][new_c]
            if alpha[ord(target)-65]:
                alpha[ord(target)-65] = False # 내가 지금 가니까 못 가도록 막음
                dfs(new_r, new_c, depth + 1)
                alpha[ord(target) - 65] = True # 다시 갈 수 있도록 함
                
                
alpha[ord(graph[0][0]) - 65] = False
dfs(0, 0, 1)
print(ans)

