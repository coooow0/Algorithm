import sys
input = sys.stdin.readline

u, n = map(int, input().strip().split())

arr = [[] for _ in range(u + 1)]

for _ in range(n):
    name = list(input().strip().split())
    
    arr[int(name[1])].append(name[0])


name = 0
money = 0

cnt  = 10000000

for i in range(1, u+1):
    if arr[i]:
        cnt = min(cnt, len(arr[i]))
    
for i in range(1, u + 1):
    if len(arr[i]) == cnt:
        print(arr[i][0], i)
        exit()
        
