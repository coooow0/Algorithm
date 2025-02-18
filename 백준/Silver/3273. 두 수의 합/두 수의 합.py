n = int(input()) # 수열의 크기
arr = sorted(list(map(int, input().split())))
x = int(input()) # 자연수 두개를 더했을 때 나와야 하는 수

cnt = 0
# 두 수의 합이 x보다 크면 right의 위치를 -1 함
# 두 수의 합이 x보다 작을 경우 left의 위치를 +1 함
# 같을 경우에도 left에 +1 하기
left = 0
right = n - 1
while left < right:
    temp = arr[left] + arr[right]

    if x < temp:
        right -= 1
    elif x > temp:
        left += 1
    else:
        cnt += 1
        left += 1

print(cnt)