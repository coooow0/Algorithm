from collections import deque
import sys
print = sys.stdout.write
input = sys.stdin.readline

d = [(-1, 0),(1, 0), (0, -1), (0, 1)]

n, k = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
s, r, c = map(int, input().strip().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
            # graph[i][j] -> 바이러스의 번호, 퍼지는 우선 순위가 중요
            # i, j -> 현재 위치. 어디서 퍼질지를 알기 위해서
            # 바이러스 번호를 기준으로 정렬해야돼서 저장함 
            # 번호가 낮은 종류의 바이러스부터 먼저 증식
virus.sort()

queue = deque()
for v_num, row, col in virus:
    queue.append((v_num, row, col, 0))
    # 바이러스 번호, 행, 열, 시간을 저장
    
while queue:
    v_num, row, col, time = queue.popleft()
    
    if time == s:
        break
    
    for dr, dc in d:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < n and 0 <= new_c < n:
            if graph[new_r][new_c] == 0:
                graph[new_r][new_c] = v_num
                queue.append((v_num, new_r, new_c, time + 1))
                # 현 위치의 바이러스 번호와 탐색할 다음위치, 시간을 입력받음
 
print(str(graph[r - 1][c - 1]))