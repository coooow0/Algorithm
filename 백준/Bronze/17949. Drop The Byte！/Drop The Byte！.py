import sys
input = sys.stdin.readline

line = input().strip() # 암호를 입력받음

n = int(input())

type = list(input().strip().split())

alpha = {'a': 10, 'b':11, 'c':12, 'd':13, 'e': 14, 'f': 15}

left, right = 0, 0

ans = []

for text in type: # 각 타입마다
    if text == 'char': # 문자일 경우
        right += 2 # 2개 가져와야함
        ans.append(int(line[left:right], 16)) 
        
        left += 2
        
    elif text == 'int':
        right += 8
        ans.append(int(line[left:right], 16)) 
        
        left += 8
        
    else:
        right += 16
        ans.append(int(line[left:right], 16)) 
        
        left += 16
    
for i in ans:
    print(i, end=' ')