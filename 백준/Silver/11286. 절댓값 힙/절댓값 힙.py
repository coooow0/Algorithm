import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

plus = []
minus = []

for _ in range(n):
    x = int(input().strip())
    
    if x < 0:
        # 음수의 경우
        heapq.heappush(minus, -x)
        
    elif x > 0:
        # 양수의 경우
        heapq.heappush(plus, x)
        
    else:
        # 0일 경우 절댓값이 작은 값을 출력하고 그 값을 제거해야 함. 
        # 절댓값이 여러개일 경우 가장 작은 수를 출력하고, 그 값을 제거
        if not len(plus) and not len(minus):
            print(0)
            # 둘 다 비어있을 경우
            
        elif len(plus) == 0:
            # 양수가 없을 경우 음수를 내보냄
            print(-heapq.heappop(minus))
        
        elif len(minus) == 0:
            print(heapq.heappop(plus))
        
        else:
            # 둘 다 있을 경우
            a = plus[0]
            b = minus[0]
            
            if a > b:
                # 양수의 절댓값이 더 큰 경우 음수를 내보내야 함
                print(-heapq.heappop(minus))
            elif b > a:
                # 음수의 절댓값이 더 큰 경우 양수를 내보내야 함
                print(heapq.heappop(plus))
            else:
                # 둘이 같은 경우
                print(-heapq.heappop(minus))
                # 작은 값ㅇ르 내보냄