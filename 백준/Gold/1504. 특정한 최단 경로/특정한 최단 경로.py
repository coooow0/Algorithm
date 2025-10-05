# 방향성이 없는 그래프 -> 양방향?
# 1 -> n 번 정점까지 최단거리
# 주어진 두 정점은 무조건 통과

# 한번 이동했던 정점은 물론, 이동했던 간선 재활용도 가능 -> 최단거리기만 하면 됨
# 두 정점 무조건 통과하는 방식

import heapq
import sys
input = sys.stdin.readline


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
must_a, must_b = map(int, input().split()) # 꼭 거쳐야하는 정점

INF = 1000 * 200000

# 다익스트라: 출발 점으로 부터 나머지 점까지의 최단 거리를 구하는 거
def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    
    heapq.heappush(queue, (0, start))
    
    while queue:
        cnt, num = heapq.heappop(queue)
        
        if cnt > distance[num]:
            continue
        
        for next, value in graph[num]:
            new_v = cnt + value
            
            if distance[next] > new_v:
                heapq.heappush(queue, (new_v, next))
                distance[next] = new_v
    return distance

d1 = dijkstra(1) # 1 -> 모든 정점

d2 = dijkstra(must_a) # must_a -> 나머지 정점 최단 
d3 = dijkstra(must_b) # must_b -> 나머지 정점 최단

res = min(d1[must_a] + d2[must_b] + d3[n], d1[must_b] + d3[must_a] + d2[n])
# d1[must_a] = 1번에서 must_a까지, d2[must_b] = must_a 에서 must_b
# d1[must_b] = 1번에서 must_b까지, d3[must_a] = must_b에서 must_a
print(-1 if res >= INF else res)