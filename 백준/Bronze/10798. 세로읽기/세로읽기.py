# 세로읽기
import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(list(map(str, input().strip())))
    
ans = ''
max = 0
for i in range(5):
    if len(arr[i]) > max:
        max = len(arr[i])
    
for i in range(max):
    for k in range(5):
        if len(arr[k]) > i:
            ans += arr[k][i]

print(ans)