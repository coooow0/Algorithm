import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dirR = [1, -1, 0, 0] # 행 
dirC = [0, 0, 1, -1] # 열

def dfs(y, x):
    graph[y][x] = False
    
    for next in range(4):
        new_x = dirC[next] + x
        new_y = dirR[next] + y
        if graph[new_y][new_x]:
            dfs(new_y, new_x)

t = int(input()) # 테스트 케이스 입력받음
for _ in range(t):
    m, n, k = map(int, input().split())
    # 가로, 세로, 배추 개수 
    graph = [[False] * (m + 2) for _ in range(n + 2)]
    # 0인 칸은 아예 안 씀. 넉넉하게 한 칸 씩 더 부여해줌!
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True
    
    answer = 0
    for i in range(1, n + 2): # 열 
        for k in range(1, m + 2): # 행
            if graph[i][k]: # True일 경우
                dfs(i, k) 
                answer += 1
    print(answer)
                  