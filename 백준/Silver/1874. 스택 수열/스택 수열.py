import sys
n = int(sys.stdin.readline())
count = 1 
stack = []
result = []

for _ in range(n):
    num = int(sys.stdin.readline())
    # 입력한 임의의 수열이 count보다 작으면 빠져나옴
    # 예제를 보면 n=8, 임의의 수열 중 첫번째 수가 4임
    # 그러면 카운트는 5가 되었을 때 빠져나옴
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        print('NO')
        break
else :
    for i in result:
        print(i)