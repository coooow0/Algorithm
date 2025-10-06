import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n + 1)]
queue = []

INF = 1000 * 100000
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    r, c, v = map(int, input().split())
    graph[r].append((c, v))

start, end = map(int, input().split())

distance[start] = 0
heapq.heappush(queue, (0, start))
pre_node = [0 for _ in range(n + 1)] # pre_node[a] = b 의 경우 a에 가려면 b를 거쳐와야함. 같은 배열.. 

def dijkstra(s):
    while queue:
        cnt, num = heapq.heappop(queue)
        
        if cnt > distance[num]:
            continue
        
        for next, next_v in graph[num]:
            new_v = next_v + cnt
            if distance[next] > new_v:
                heapq.heappush(queue, (new_v, next))
                distance[next] = new_v
                pre_node[next] = num
        
res = []
e = end
dijkstra(start)
while True:
    res.append(e)
    
    if e == start:
        break
    
    e = pre_node[e]
# res.reserve()
print(distance[end])
print(len(res))
print(*res[::-1])