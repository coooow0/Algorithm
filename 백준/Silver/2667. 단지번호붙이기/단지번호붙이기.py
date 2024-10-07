import sys
sys.setrecursionlimit(10 ** 6)

def dfs(row, col):
    arr[all_cnt] += 1
    graph[row][col] = 0
    for i, k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_R = i + row
        new_C = k + col
        if graph[new_R][new_C] == 1:
            dfs(new_R, new_C)


arr = [0]
n = int(input())

# 마찬가지로 그래프를 만드는데 0인 곳은 제외하고 1부터 시작. 상하 좌우를 탐지해야하니 넉넉히 두 칸을 더 넣어줌
graph = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input())) + [0]
    # 상하좌우를 확인을 해야돼서.. 앞 뒤로 한 칸씩 더 만들어줌

all_cnt = 0 #단지 수를 출력

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if graph[row][col] == 1: # 1이면
            dfs(row, col)
            all_cnt += 1
        arr.append(0) # 단지수에 따라서 늘어나기 때문에 추가해줌
            
print(all_cnt)

arr.sort()
arr = arr[-all_cnt:]
for i in arr:
    print(i)