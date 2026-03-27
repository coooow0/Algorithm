import sys
input = sys.stdin.readline

x, y, p1, p2 = map(int, input().strip().split())
# p는 시작 지점 
graph = [False for _ in range(10001)]


while p1 <= 10001 and p2 < 10001:
    
    if graph[p1]:
        print(p1)
        exit()
    elif graph[p2]:
        print(p2)
        exit()
        
    else:
        graph[p1] = True
        graph[p2] = True
        
        p1 += x
        p2 += y
print(-1)