# # 요세푸스 문제
from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])

answer = []

while d:
    for _ in range(k-1):
        d.append(d.popleft())
    answer.append(d.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))

