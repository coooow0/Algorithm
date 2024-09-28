# 집합
import sys
input = sys.stdin.readline

n = int(input())

s = set()

for i in range(n):
    arr = input().rstrip().split()
    if arr[0] == 'add':
        s.add(int(arr[1]))
    elif arr[0] == 'check':
        print(1 if int(arr[1]) in s else 0)
    elif arr[0] == 'remove':
        s.discard(int(arr[1]))  # remove 대신 discard를 쓰면, 존재하지 않아도 에러가 발생하지 않음
    elif arr[0] == 'toggle':
        x = int(arr[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif arr[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif arr[0] == 'empty':
        s.clear()
