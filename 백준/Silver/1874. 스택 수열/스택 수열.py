# 스택 


n = int(input())

stack = []

m = 1
str = []

s = True

for _ in range(n):
    a = int(input())
    
    while m <= a:
        stack.append(m)
        str.append('+')
        m += 1
    
    if stack[-1] == a:
        stack.pop()
        str.append('-')
        
    else:
        s = False
if s:
    for i in str:
        print(i)
else:
    print("NO")