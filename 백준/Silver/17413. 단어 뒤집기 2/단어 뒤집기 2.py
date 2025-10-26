# 띄어쓰기만 있는 경우
# 띄어쓰기와 괄호가 있는 경우
# 괄호만 있는 경우
# 둘 다 없는 경우


import sys
input = sys.stdin.readline

line = list(map(str, input()))

res = '' # 정답을 집어넣음
tmp = '' # 뒤집을 문자열을 넣음

rev = False

for i in line:
    if i == '<':
        
        res += tmp[::-1]
        res += i
        tmp = ''
        rev = True
        
    elif i =='>':
        res += i
        rev = False
        
    elif i == ' ':
        if rev: # 안 뒤집어도 ㄱㅊ으면
            res += i
        else: # 뒤집어야 할 경우
            res += (tmp[::-1])
            res += i 
            tmp = ''
            
    elif i == '\n':
        res += tmp[::-1]
        
    else: # 일반 문자가 들어왔을 때
        if rev:
            res += i
        else:
            tmp += i
    
print(res)