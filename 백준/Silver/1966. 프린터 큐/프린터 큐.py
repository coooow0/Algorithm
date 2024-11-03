#  프린터 큐
from collections import deque
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().strip().split())
    # 문서 개수, 궁금한 큐
    arr = deque()
    arr += list(map(int, input().split()))

    ans = arr[m] # 원하는 값을 저장해둠..
    cnt = 0

    idx = deque()
    idx += [i for i in range(n)]
    # 원하는 인덱스가 맞는지 확인하기 위해
    
    while True:
        if arr[0] == max(arr):
            cnt += 1
            
            if idx[0] == m:
                print(cnt)
                break
            else:
                # 앞에 수도 다 같은 수
                del arr[0]
                del idx[0]
                
        else:
            arr.append(arr.popleft())
            idx.append(idx.popleft())