import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

for i in range(3):
    bowwow = True # 초기 상태는 짖음이 상태 
    genzai = 1 + (a - 1) # 현 상태 맨 처음에는 짖음이
    
    cnt = 0
    
    while genzai < arr[i]:
        if bowwow: # 현재 짖음이 상태면 
            bowwow = False # 바꿔주고
            genzai += b 
    
        else:
            bowwow = True
            genzai += a 
    if bowwow: cnt += 1
    
    
    genzai = 1 + (c - 1)
    bowwow = True
    
    while genzai < arr[i]:
        if bowwow:
            bowwow = False
            genzai += d
            
        else:
            bowwow = True
            genzai += c
    
    if bowwow: cnt += 1
    print(cnt)