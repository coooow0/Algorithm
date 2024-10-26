m, h = map(int, input().split())
tree = list(map(int, input().split()))

left, right = 1, max(tree)

while left <= right:
    mid = (left + right) // 2 
    cnt = 0
    
    for num in tree:
        if mid < num:
            cnt += num - mid
        
    if cnt >= h:
        left = mid + 1
    
    else:
        right = mid - 1

print(right)