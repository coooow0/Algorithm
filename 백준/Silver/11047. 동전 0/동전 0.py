import sys
input = sys.stdin.readline

n , k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
cnt = 0
for num in arr:
    if k >= num:
        cnt += k // num
        k = int(k % num)
        
print(cnt)