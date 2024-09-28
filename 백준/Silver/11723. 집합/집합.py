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
        if int(arr[1]) in s:
            print(1)
        else: print(0)
    elif arr[0] == 'remove':
        s.discard(int(arr[1])) # 삭제하려는 것이 없어도 오류가 나지 않음. remove는 오류가 나서 if문을 통해 확인해야함
    elif arr[0] == 'toggle':
        x = int(arr[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif arr[0] == 'all':
        s = {i for i in range(1, 21)}
    else:
        s = set()
