import sys
input = sys.stdin.readline

while True:
    i = 1
    cnt = 1
    
    try:
        n = int(input())
        
        while i % n != 0:
            i = (i * 10 + 1) % n
            # 나머지 연산.. 
            cnt += 1
            
        print(cnt)
            
    except:
        break