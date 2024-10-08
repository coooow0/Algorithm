# 최소 힙
import sys
import heapq
# 자동으로 힙을 만들어줌
input = sys.stdin.readline
n = int(input().strip())
arr = []
for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if len(arr): # 1 이상
            print(heapq.heappop(arr))
            # 맨 위에 있는 작은 수를 pop
        else:
            print(0)
    else:
        heapq.heappush(arr, x)
        # x를 집어넣는데 알아서 정리됨
        