import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
tomato = [list(map(int, input().strip().split())) for _ in range(m)]

queue = deque()

for row in range(m): # 행
    for col in range(n): # 열 
        if tomato[row][col] == 1:
            queue.append([row, col])
            # 1인 애들을 모두 큐에 집어넣음 

def bfs():
    while queue: # 텅텅이 될 때 까지
        row, col = queue.popleft() # 1인 위치
        for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r = row + r
            new_c = col + c
            if 0 <= new_r < m and 0 <= new_c < n: # 그래프보다 작거나 큰 숫자를 받은 경우 안됨...
                if tomato[new_r][new_c] == 0: # 0인 경우 바꿔주기
                    # 익히고 1을 더해서 개수를 세어줌.. 여기서 제일 큰 값이 최소 날짜
                    tomato[new_r][new_c] = tomato[row][col] + 1
                    queue.append([new_r, new_c])
                    
bfs()

days = 0
for i in tomato:
    for k in i:
        if k == 0:
            print(-1)
            exit()
        # 입력받을 때 다 익은 경우를 생각하면 어차피 제일 큰 값은 1. 거기서 1을 빼주면 0이 돼서 
        # 그 경우는 생략
    days = max(days, max(i))
print(days - 1)