import sys
import heapq

input = sys.stdin.readline
queue = []


n = int(input()) # 도시 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    r, c, v = map(int, input().split())
    graph[r].append((c, v)) # 도시와 가중치를 집어넣음....

start, end = map(int, input().split()) # 출발 도시, 도착 도시

INF = 100000 * 1000 # m * n 최대 개수만큼 곱함. 큰 값으로 설정ㅇㅇ
distance = [INF for _ in range(n + 1)] # 최단 거리 테이블

heapq.heappush(queue, (0, start)) # 처음 시작 값은 0. 하나의 시작 점만 넣고 시작
distance[start] = 0 # 나에게 가는 값은 0임

def dijkstra():
    while queue:
        cnt, num = heapq.heappop(queue) # cnt에는 제일 작은 값이 나옴, num에는 도시 번호
        
        if distance[num] < cnt:
            continue
        # 더 짧은 경로를 아는 경우 무시
        
        for dr, dc in graph[num]: # 다음 도시, 가중치
            new_cost = cnt + dc
            
            if new_cost < distance[dr]:
                distance[dr] = new_cost
                heapq.heappush(queue, (new_cost, dr))
    
    return distance[end]

print(dijkstra())

