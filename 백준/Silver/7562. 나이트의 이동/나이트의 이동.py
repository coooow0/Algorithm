import sys
input = sys.stdin.readline
from collections import deque

d = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

def bfs():
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in d:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < l and 0 <= new_c < l:
                if graph[new_r][new_c] == 0:
                    graph[new_r][new_c] = graph[row][col] + 1
                    queue.append((new_r, new_c))
            if new_r == nr and new_c == nc:
                return print(graph[row][col])
                

T = int(input().strip())

for i in range(T):
    # 첫 줄에 체스판 한 변의 길이
    l = int(input())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    
    # 둘째, 셋째 줄에 나이트가 있는 칸, 이동하려고 하는 칸
    r, c = map(int, input().strip().split())
    queue.append((r,c))
    graph[r][c] = 1
    
    nr, nc = map(int, input().strip().split())
    # 최소 몇번 만에 갈 수 있는가
    if r == nr and c == nc:
        print(0)    
    else:
        bfs()
    