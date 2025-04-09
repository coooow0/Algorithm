# CD
import sys
input = sys.stdin.readline

while True:  
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    a = []
    for _ in range(n):
        a.append(int(input()))
        
    b = []
    for _ in range(m):
        b.append(int(input()))
    
    first = 0 # a를 탐색할 변수
    second = 0 # b를 탐색할 변수

    cnt = 0

    while first < n and second < m:
        # 해당 조건을 만족할때만 동작
        cd_1, cd_2 = a[first], b[second]
        if cd_1 < cd_2:
            first += 1
        elif cd_1 > cd_2:
            second += 1
        else:
            cnt += 1
            first += 1
            second += 1
    print(cnt)