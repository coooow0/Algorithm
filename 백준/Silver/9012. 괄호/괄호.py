import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    string = list(input())
    count = 0
    for j in range(len(string)):
        if string[j] == '(':
            count += 1
        elif string[j] == ')':
            count -= 1
        #^^... .j랑 i 구분 잘 하기.. 
        if count < 0:
            #만약 ))가 두개면 제대로 안 닫힌 거
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        #else로 했는데 count < 0인 경우를 까먹음 ㅜ
        print('YES')
