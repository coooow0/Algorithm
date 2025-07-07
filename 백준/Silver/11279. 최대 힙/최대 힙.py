import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

heap = []
# 힙 자체는 최소 힙이 기본전제. 작은 수가 부모노드

for _ in range(n):
    x = int(input().strip())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
            
    else:
        heapq.heappush(heap, -x)
        # 따라서 입력받은 수에 - 부호를 붙임. 그래야 제일 큰 수가 -부호를 받고 제일 작아지니까
    