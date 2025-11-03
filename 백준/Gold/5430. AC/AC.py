from collections import deque
import sys
input = sys.stdin.readline 

t = int(input().strip())

for _ in range(t):
    line = list(input().strip())
    
    n = int(input().strip()) # 배열에 들어있는 수의 개수
    
    num = input().strip()
    num = num.replace('[', '').replace(']', '')
    num = deque(num.split(','))
    
    isReversed = False
    error = False
    for i in line:
        if i == 'R':
            if isReversed:
                isReversed = False
            else:
                isReversed = True
            
        else:
            # D의 경우
            if n == 0:
                print('error')
                error = True
                break
        
            if isReversed: # 뒤집힌 경우
                n -= 1
                num.pop()
            else:
                n -= 1
                num.popleft()
                
    num = list(num)
    
    if error:
        continue
    else:
        if isReversed: # 뒤집힌 경우
            print('[', end='')
            print(*num[::-1],sep=',', end='')
            print(']')
         
        else:
            print('[', end='')
            print(*num, sep=',', end='')
            print(']')