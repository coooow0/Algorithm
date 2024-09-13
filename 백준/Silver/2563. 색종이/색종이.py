n = int(input())

arr = [[0] * 100 for _ in range(100)]
# 색종이의 크기 100, 최대 100장(range)

for i in range(n):
    a, b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            arr[x][y] = 1

cnt = 0

for i in range(100): #최대 100장
    cnt += sum(arr[i])
print(cnt)