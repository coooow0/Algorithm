from collections import deque

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = deque([i for i in range(1, n+1)])
ysps = []

while len(arr) != 0:
    for i in range(k-1):
        arr.append(arr.popleft())
    ysps.append(arr.popleft())

print('<'+', '.join(map(str, ysps))+'>')