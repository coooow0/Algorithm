n, m = map(int, input().split())

a = list()
for _ in range(n):
    a.append(list(map(int, input().split())))

b = list()
for _ in range(n):
    b.append(list(map(int,input().split())))
    

for i in range(n):
    for k in range(m):
        a[i][k] += b[i][k]

for i in range(n):
    print(*a[i])