# 주사위를 던져 100에 먼저 도착하는 것이 무조건 최단시간.
# bfs가 최단 시간을 구하는 거니까.. 먼저 도착한 순으로 방문을 하고 그게 값이 커지면 100에 먼저 닿을 수 밖에 없음


from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    
    while queue:
        now, time = queue.popleft()
        # 지금 좌표랑 시간
        
        for i in range(1, 7):
            # 주사위를 1 - 6까지 던짐이
            if now == 100:
                print(time)
                break
            next = now + i
            if next <= 100:
                if next in snake.keys():
                    # 주사위를 던진 위치가 뱀의 자리에 있을 경우 이동을 함
                    next = snake[next]
                    
                if next in ladder.keys():
                    next = ladder[next]
                    
                if not visited[next]:
                    visited[next] = True
                    queue.append((next, time + 1))
                


n, m = map(int, input().strip().split())

visited = [False for _ in range(101)]
queue = deque()

ladder = {}
snake = {}

for _ in range(n):
    start, end = map(int, input().strip().split())
    ladder[start] = end
    # 작은 수에서 큰 수로 이동
    
for _ in range(m):
    start, end = map(int, input().strip().split())
    snake[start] = end
    # 큰 수에서 작은 수로 이동함
    
visited[1] = True
# 1에서 시작하니까 참으로 설정

queue.append((1, 0))
# 현 위치와 던진 주사위 횟수
bfs()

