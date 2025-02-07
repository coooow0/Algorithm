from collections import deque
n, m = list(map(int, input().split()))
# 큐의 크기 n, 뽑으려는 수의 개수 m

arr = deque([i for i in range(1, n + 1)])
num = list(map(int, input().split()))

cnt = 0

while len(num) != 0:
    if arr[0] == num[0]:
        arr.popleft()
        num.pop(0)
    else:
        target = arr.index(num[0])
        # 빼야 하는 것의 위치를 구함
        if target > len(arr) - target:
            # 더 적은 것을 선택해서 그만큼 rotate 함
            cnt += len(arr) - target
            arr.rotate(len(arr) - target)
        else:
            cnt += target
            arr.rotate(-target)
print(cnt)