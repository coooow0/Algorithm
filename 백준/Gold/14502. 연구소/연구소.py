from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def start():
    queue = deque(virus)
    v_count = 0
    
    while queue:
        vrow, vcol = queue.popleft()
        # 바이러스의 위치. 그래서 상하좌우를 살피어야함. 0이면 카운트 ㄱㄱ 하고 큐에 넣음. 
        
        for nr, nc in dir:
            next_row, next_col = nr + vrow, nc + vcol 
            
            if 0 <= next_row <n and 0 <= next_col < m:
                # 범위 이내이고.. 
                if temp_arr[next_row][next_col] == 0:
                    queue.append((next_row, next_col))
                    temp_arr[next_row][next_col] = 2
                    v_count += 1
                    
    return v_count
    
arr = []

zero = []
virus = deque()

for i in range(n):
    arr.append(list(map(int, input().split())))
    for k in range(m):
        if arr[i][k] == 0:
            zero.append((i, k))
            
        if arr[i][k] == 2:
            virus.append((i, k))

safety = len(zero) # 안전구역의 수 

combo = (combinations(zero, 3))

cnt = 0

for walls in combo: #ex. ([2, 4], [3, 3], [3, 4])
    temp_arr = [row[:]for row in arr]
    
    for r, c in walls:
        temp_arr[r][c] = 1
    
    # print(start()) # 현재 바이러스 넓게 퍼뜨리기
    cnt = max(cnt, safety - start() - 3)
    
print(cnt)

