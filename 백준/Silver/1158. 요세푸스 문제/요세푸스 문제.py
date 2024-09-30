# 요세푸스 문제

from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])

answer = []

while d:
    d.rotate(-(k-1))
    # rotate(n)
    # n이 양수면 n칸 만큼 오른쪽으로 이동하고, 음수면 맨 뒤에서 부터 시작함..
    answer.append(d.popleft())
print(str(answer).replace('[', '<').replace(']', '>'))