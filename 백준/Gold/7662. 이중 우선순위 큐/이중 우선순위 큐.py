import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 몇 개 입력받을 거임
    n = int(input())
    
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙. 넣을 때 마이너스 붙여서 넣기
    
    dic = dict() # 안에 몇 개 있는지 찾기. key로 value 얻기 dic.get()
    
    for _ in range(n):
        a, b = map(str, input().strip().split())
        # a는 I or D, b는 숫자
        b = int(b)
        
        if a == 'I': # 더하기 
            if b not in dic:
                dic[b] = 1
            else:
                dic[b] += 1
                
            heapq.heappush(min_h, b)
            heapq.heappush(max_h, -b)
            
        else: # 빼기
            if b == -1: # 최소 힙을 제거
                while min_h and dic.get(min_h[0], 0) == 0:
                    heapq.heappop(min_h)
                    
                if min_h:             
                    dic[min_h[0]] -= 1
                    heapq.heappop(min_h)
                
            else: # 최대 힙을 제거
                while max_h and dic.get(-max_h[0], 0) == 0:
                    heapq.heappop(max_h)
                
                if max_h:
                    dic[-max_h[0]] -= 1
                    heapq.heappop(max_h)
        

    # 다 하면 마지막에 다시 확인하기
    
    while min_h and dic.get(min_h[0], 0) == 0:
        heapq.heappop(min_h)
    
    while max_h and dic.get(-max_h[0], 0) == 0:
        heapq.heappop(max_h)
        
    if min_h and max_h:
        print(-max_h[0], min_h[0])
    else:
        print('EMPTY')
                    
            