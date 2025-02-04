import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
# n행 m열의 배열이 만들어짐
arr = [[0] * m] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

prefix = [[0] * (m + 1) for _ in range(n + 1)] #누적합 배열 

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = arr[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i-1][j-1] 
        # arr[i - 1][j - 1] 원본 배열의 값
        # prefix[i-1][j-1] 중복 제거

k = int(input())
for _ in range(k):
    i, j, x, y = list(map(int, input().split()))
    res = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
    # prefix[i-1][y] -> 필요없는 행을 지움 prefix[x][j-1] -> 필요없는 열을 지움
    print(res)