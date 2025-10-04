import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split()) # 정점, 간선 개수
start = int(input()) # 시작 번호

graph= [[] for _ in range(v + 1)]
queue = []
INF = 20000 * 300000 # 최대값
distance = [INF for _ in range(v+1)] # 최단 경로를 위한 배열

for _ in range(e):
    r, c, w = map(int, input().split())
    # r -> c 로 가는 가중치 w인 간선이 있다
    graph[r].append((c, w))

distance[start] = 0 # 본인은 0으로
heapq.heappush(queue, (0, start)) # 시작점

def dijkstra():
    while queue:
        cnt, num = heapq.heappop(queue)
        
        if cnt > distance[num]:
            continue
        
        for next, next_v in graph[num]:
            if distance[next] > next_v + cnt:
                heapq.heappush(queue, (next_v + cnt, next))
                distance[next] = next_v + cnt
    
dijkstra()
for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])