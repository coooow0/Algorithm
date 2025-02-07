from collections import deque

n, m = map(int, input().split())  # 큐 크기 n, 뽑을 수 개수 m
arr = deque(range(1, n + 1))  # 원형 큐 초기화
num = deque(map(int, input().split()))  # 뽑아야 하는 숫자 리스트

cnt = 0

while num:
    target = arr.index(num[0])  # 찾을 숫자의 위치
    if target == 0:  # 맨 앞에 있으면 바로 제거
        arr.popleft()
        num.popleft()
    else:
        if target > len(arr) - target:
            # 오른쪽으로 회전 (뒤에서 앞으로 보내기)
            cnt += len(arr) - target
            arr.rotate(len(arr) - target)
        else:
            # 왼쪽으로 회전 (앞에서 뒤로 보내기)
            cnt += target
            arr.rotate(-target)

print(cnt)
