
n = int(input())
body = [[0, 0]]*n

for i in range(n): # 몸무게와 키를 입력받음
    body[i] = list(map(int, input().split())) 
    
win = [1] * n # 등수를 1로 초기화 함

for i in range(1, n):
    after = body[i] # 현재 값
    for k in range(0, i):
        if after[0] > body[k][0] and after[1] > body[k][1]: #현재 값이 클 경우
            win[k] += 1
        elif after[0] < body[k][0] and after[1] < body[k][1]: #현재 값이 더 작을 경우
            win[i] += 1

print(' '.join(list(map(str, win))))