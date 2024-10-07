# 섬의 개수
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

arr = [(1, 0), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (-1, 1), (-1, -1)]

def dfs(row, col):
    graph[row][col] = 0
    for next_r, next_c in arr:
        new_r = row + next_r
        new_c = col + next_c
        if graph[new_r][new_c] == 1:
            dfs(new_r, new_c)

while True:
    w, h = map(int, input().split())
    # 가로, 세로 길이를 받음
    if (w or h) == 0:
        break
    graph = [[0] * (w + 2) for _ in range(h + 2)] 
    # 이렇게 하는게 메모리 차원에서 안 좋은 거 같지만.. 이렇게 안하면 못 풀겠다ㅜ
    for i in range(1, h + 1):
        graph[i] = [0] + list(map(int, input().split())) + [0]
    
    answer = 0
    
    for i in range(1, h + 1): # row
        for k in range(1, w + 1): # col
            if graph[i][k] == 1:
                dfs(i, k)
                answer += 1
    print(answer)