n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

result = 0

left, right = 1, arr[-1]-arr[0]
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    standard = arr[0]
    
    for i in range(n):
        if arr[i] - standard >= mid:
            cnt += 1
            standard = arr[i]
    
    if cnt >= c:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)