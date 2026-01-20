from collections import deque

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = (list(map(int, input().strip().split()))) # 숫자
oper = list(map(int, input().strip().split())) # 연산자

min_res = 1000000000
max_res = -1000000000


def put_oper(cnt, res):
    global min_res 
    global max_res

    if cnt == n - 1:
        min_res = min(min_res, res)
        max_res = max(max_res, res)
        return 
    for i in range(4): 
        # 연산자 남아있는지 확인
        if oper[i]:
            if i == 0:
                oper[i] -= 1
                put_oper(cnt + 1, res + arr[cnt + 1])
                oper[i] += 1
                
            elif i == 1:#빼기
                oper[i] -= 1
                put_oper(cnt + 1, res - arr[cnt + 1])
                oper[i] += 1
            
            elif i == 2:#곱하기
                oper[i] -= 1
                put_oper(cnt + 1, res * arr[cnt + 1])
                oper[i] += 1
            
            else:#나누기
                oper[i] -= 1
                if res < 0:
                    put_oper(cnt + 1, -(abs(res) // arr[cnt + 1]))
                else:
                    put_oper(cnt + 1, res // arr[cnt + 1])
                oper[i] += 1
                
put_oper(0, arr[0]) # 카운트 값이랑 간이 결과값

print(max_res)
print(min_res)