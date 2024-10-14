from collections import deque
n, m = map(int, input().split())
# 크기를 입력받음

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()
queue.append([0, 0])

def bfs():
    while queue:
        row, col = queue.popleft()
        for xr, xc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r = row + xr
            new_c = col + xc 
            if 0<= new_r <n and 0<= new_c < m and arr[new_r][new_c] == 1:
                arr[new_r][new_c] = arr[row][col] + 1
                queue.append([new_r, new_c])
bfs()
print(arr[n-1][m-1])