import sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    wear = dict()
    n = int(input().strip())
    
    for _ in range(n):
        clothes, type = map(str, input().strip().split())
        if type in wear: # 안에 있으면
            wear[type] += 1
            # 어차피 개수가 중요한 거니까 clothes 자체를 따로 append하지 않음
            
        else: # 안에 없으면
            wear[type] = 1

    cnt = 1
    for x in wear:
        cnt *= (wear[x] + 1)
        # 해당 의상을 착용하지 않은 경우를 포함하기 위해 1을 더함 
        # 한 종류의 옷이 2개일 경우, 총 세개의 경우가 나옴.  
        # 아무것도 안 입을 경우, a를 선택할 경우, b를 선택할 경우 따라서 1을 더함.. 
        
    print(cnt - 1)
    # 위에 + 1을 하여 더한 것 때문에 1을 빼줌. 
    # 아예 아무것도 선택하지 않을 경우가 있기 때문에 1을 제외!! 알몸일경우...//