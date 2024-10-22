k, n = map(int, input().split())
# 현재 갖고있는 랜선 개수 k, 필요로 하는 랜선 개수 n
arr = list()
for _ in range(k):
    arr.append(int(input()))

left, right = 1, max(arr)

while right >= left:
    mid = (right + left) // 2
    lan = 0
    for i in range(k):
        lan += arr[i] // mid
    
    if n > lan:
        right = mid - 1
    else:
        left = mid + 1
print(right)