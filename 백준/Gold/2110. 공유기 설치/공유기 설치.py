# 공유기 설치

n, c = map(int, input().split())
# 집의 개수, 공유기의 수
house = []
for _ in range(n):
    house.append(int(input()))
# 집의 좌표
house.sort()

left, right = 1, house[-1]-house[0]
result = 0

while right >= left:
    mid = (left + right) // 2
    # 중앙 수
    cnt = 1
    # mid 거리만큼 거리두었을 때 공유기의 개수를 셈
    stand = house[0]
    
    for i in range(1, n):
        if house[i] >= stand + mid:
            cnt += 1
            stand = house[i]
    # print(cnt)
    if cnt >= c:
        # cnt가 더 크면? mid가 너무 작다는 것. 하나 더 더함
        result = mid
        left = mid + 1
    
    else:
        right = mid - 1
        
print(result)