from collections import deque

n = int(input())

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    while queue:
        row, col = queue.popleft()
        
        for nr, nc in dir:
            new_r, new_c = nr + row, nc + col
            
            if 0<= new_r < n and 0 <= new_c < n: # 범위 이내이고
                if temp_graph[new_r][new_c] != 0:
                    temp_graph[new_r][new_c] = 0
                    queue.append((new_r, new_c))
    


graph = [] # 원본 2차원 배열
arr = [] # set용 배열

for i in range(n):
    graph.append(list(map(int, input().split())))
    arr += graph[i]
arr = list(set(arr))
arr.sort()

cnt = 1
for i in arr:
    no_water = 0
    queue = deque()
    # 제일 작은 수부터 0으로 만들어서 잠기게 표시하기
    for j in range(n):
        for k in range(n):
            if graph[j][k] == i:
                graph[j][k] = 0
    # print(graph)
    temp_graph = [row[:] for row in graph] # 0으로 덮어 씌운 그래프를 복사함
    
    for r in range(n):
        for c in range(n):
            if temp_graph[r][c] != 0:
                # 안 잠긴 곳을 넣고 bfs 실행해서 덩어리 세기 
                temp_graph[r][c] = 0
                queue.append((r, c))
                
                bfs() # 넣고 기준으로 덩어리 세기 
                no_water += 1

    cnt = max(cnt, no_water )
print(cnt)