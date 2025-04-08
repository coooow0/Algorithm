# 행렬곱
n, m = map(int, input().split()) #n행 m열
a = [[] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int,input().split()))

m, p = map(int, input().split()) #m행 p열
b = [[] for _ in range(m)]

for i in range(m):
    b[i] = list(map(int, input().split()))

c = [[0 for _ in range(p)] for _ in range(n)]
# 행렬곱의 크기는 n * p

for i in range(n): # row
    for j in range(p): # col
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
            
for i in range(n):
    print(*c[i])