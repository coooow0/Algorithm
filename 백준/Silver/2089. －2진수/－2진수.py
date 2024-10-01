# -2진수 
n = int(input())
if n == 0:
    print(0)
    exit()
    
answer = ''

while n:
    if n % -2: # 나머지가 -1인 경우
        answer += '1'
        n = n // -2 + 1
    else:
        answer += '0'
        n = n // -2
        
print(answer[::-1])