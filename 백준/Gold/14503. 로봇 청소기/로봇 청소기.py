import sys
input = sys.stdin.readline

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 동서남북 

n, m = map(int,input().strip().split())

r, c, d = map(int, input().strip().split())
# 로청 위치랑 바라보는 방향
graph=[]

for _ in range(n):
    graph.append(list(map(int, input().strip().split())))
    
cnt = 0
           
# 청소 안 된 칸이 없으면 = 청소된 칸이 4개면
# 청소되기 않은 빈 칸이 있으면 = 하나라도 청소가 안 되어 있으면. 0인 칸이 하나라도 있으면 
while True:
    if graph[r][c] == 0:
        # 청소가 안 된 칸이면
        graph[r][c] = -1
        # -1로 청소된 칸을 표시함
        cnt += 1

    clean = 0 # 청소가 된 칸을 센다. 

    for dr, dc in dir:
        new_r, new_c = r + dr, c + dc
        
        if 0<= new_r < n and 0<= new_c <m:
            # 범위 이내이고
            if graph[new_r][new_c] != 0:
                clean += 1
    
    if clean == 4:
        # 다 청소되어있으면 방향을 유지한채, 후진할 수 있으면 한칸 후진하고, continue
        # 뒤쪽 칸이 벽이라 후진할 수 없으면 멈춤
        new_r, new_c = r + (-dir[d][0]), c + (-dir[d][1])
        
        if graph[new_r][new_c] == 1:
            
            break
        else:
            r, c = new_r, new_c
            continue
    
    else:
        # 다 청소는 안 되어잇으묜 
        if d == 0:
            d = 3
        else:
            d -= 1

        new_r, new_c = r + dir[d][0], c + dir[d][1]
        # 갱신하고 
        if 0 <= new_r < n and 0<= new_c <m:
            if graph[new_r][new_c] == 0:
                r, c = new_r, new_c
                continue
            
print(cnt)