import sys
input = sys.stdin.readline().strip

def stick(arr):
    arr = list(arr)
    stack = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(': # 여는 괄호
            stack.append('(')
        else: #닫는 괄호면
            stack.pop()
            if arr[i - 1] == ')': # 이 전 배열이 )였으면 레이저이므로, 
                cnt += 1
            else: # 이 전 배열이 ( 이면 지금은 레이저. 
                cnt += len(stack)
    return cnt
                
n = input()
print(stick(n))