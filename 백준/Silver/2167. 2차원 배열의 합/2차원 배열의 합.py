import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
# n행 m열의 배열이 만들어짐
arr = [[0] * m] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

k = int(input())

for _ in range(k):
    res = 0
    i, j, x, y = list(map(int, input().split()))
    if i == x:
        for a in range(j - 1, y):
            res += arr[i - 1][a]
        print(res)

    elif j == y:
        for a in range(i - 1, x):
            res += arr[a][j - 1]
        print(res)

    else:
        for a in range(i - 1, x): # 행
            for b in range(j - 1, y): # 열
                res += arr[a][b]
        print(res)