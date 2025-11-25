m = int(input())
d = int(input())

if m == 2 and d == 18:
    print('Special')
    
elif m > 2: # 내가 적은 게 더 큰 경우
    print('After')
    
elif m == 2:
    if d > 18:
        # 더 크면
        print('After')
    else:
        print('Before')
        
elif m == 1:
    print('Before')