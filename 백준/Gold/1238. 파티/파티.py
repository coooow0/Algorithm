import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
# x가 end점이라고 하지만!!!? e에서 시작한다고 생각 ㄱ

INF = 1000 * 10000 
graph_first= [[] for _ in range(n + 1)] # 정방향
graph_second = [[] for _ in range(n+1)] # 역방향

distance1 = [INF for _ in range(n + 1)]
distance2 = [INF for _ in range(n + 1)]

queue = []

distance1[x] = 0
distance2[x] = 0
for _ in range(m):
    r, c, v = map(int, input().split())
    graph_first[r].append((c, v))
    graph_second[c].append((r, v))

def dijkstra(arr, dis):
    while queue:
        cnt, num = heapq.heappop(queue)
        if cnt > dis[num]:
            continue
        
        for next, next_v in arr[num]:
            new_v = next_v + cnt
            
            if dis[next] > new_v:
                heapq.heappush(queue, (new_v, next))
                dis[next] = new_v
    
heapq.heappush(queue, (0, x))
dijkstra(graph_first, distance1)

heapq.heappush(queue, (0, x)) # 큐 한 번 더 초기화!! 중요
dijkstra(graph_second, distance2)

res = 0
for i in range(1, n + 1):
    res = max(distance1[i] + distance2[i], res)
print(res)