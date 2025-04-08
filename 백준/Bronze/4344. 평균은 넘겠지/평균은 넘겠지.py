import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    avr = sum(arr[1:]) / arr[0]
    
    cnt = 0
    for i in range(1, arr[0]+ 1):
        if arr[i] > avr:
            cnt += 1
    
    ans = round(cnt / arr[0] * 100, 3)
    ans = str('{:.3f}'.format(ans))
    print(ans+'%')