import sys
input = sys.stdin.readline

n, m =[*map(int, input().split())]

arr = []
for i in range(n):
    arr.append([*map(int, input().split())])

prefix = [ [0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 행
    for k in range(1, n + 1): # 열
        prefix[i][k] = arr[i - 1][k - 1] + prefix[i - 1][k] + prefix[i][k - 1] - prefix[i - 1][k - 1]
# print(prefix)
for _ in range(m):
    i, k, x, y = [*map(int, input().split())]
    #x행 y열
    
    ans = prefix[x][y] - prefix[i - 1][y] - prefix[x][k - 1] + prefix[i - 1][k - 1]
    print(ans)