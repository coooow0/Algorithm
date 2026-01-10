import heapq

n = int(input())

heap = []

for _ in range(n):
    arr = list(map(int, input().strip().split()))
    
    for i in arr:
        heapq.heappush(heap, i)
    
    # 모든 수를 기억하지 말고, n개의 수만 기억하기. 
    # n개가 초과되면 제일 작은 수부터 지우기. 
    while len(heap) > n:
        heapq.heappop(heap)
        
print(heap[0])