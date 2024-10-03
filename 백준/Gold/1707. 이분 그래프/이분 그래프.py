from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, graph, color):
    q = deque([start]) # 처음 정점을 배열에 넣어줌
    color[start] = 1
    
    while q:
        now = q.popleft()
        for next in graph[now]: # 인접 리스트에서 이웃 노드를 가져옴
            if not color[next]: # 방문하지 않았다면, 반대되는 색을 칠함
                color[next] = - color[now]
                q.append(next)
            elif color[next] == color[now]: #색이 칠해져있는데 같은 색인 경우
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    
    for _ in range(e): # 연결된 노드를 입력받음
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        # v * v 크기의 그래프를 전체 다 돌지 않아도 됨. 있는거만 추가하미.. 
        # 메모리 초과가 일어나지 않도록 한다... 
        
        
        is_bipartite = True
        
    for i in range(1, v + 1):
        if not color[i]: # 방문하지 않은 노드면
            if not bfs(i, graph, color): # 이분 그래프가 아니면
                 is_bipartite = False
                 
    print('YES' if is_bipartite else 'NO')