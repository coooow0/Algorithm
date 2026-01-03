import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    heapq.heappush(arr, int(input()))
    
res = 0
while len(arr) != 1:
    cnt = heapq.heappop(arr)
    cnt += heapq.heappop(arr)
    res += cnt 
    heapq.heappush(arr, cnt)
print(res)