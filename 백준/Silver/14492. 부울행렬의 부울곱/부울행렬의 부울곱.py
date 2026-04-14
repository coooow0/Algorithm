import sys
input = sys.stdin.readline

n = int(input().strip())

a = [list(map(int, input().strip().split())) for _ in range(n)]
b = [list(map(int, input().strip().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        res = False
        for k in range(n):
            if a[i][k] == 1 and b[k][j] == 1:
                res = True
        
        if res:
            cnt += 1
print(cnt)