while True:
    t = list(map(int, input().split()))
    t.sort()
    
    if t[0] == 0 or t[1] == 0 or t[2] == 0:
        break
    else:
        t[2]= t[2]**2
        if t[2] == t[0]**2 + t[1]**2:
            print('right')
        else:
            print('wrong')
