arr = list(input())

num = 0
res = 0

for i in range(len(arr)):
    if arr[i] == '*':
        num = i #짝수면 그냥, 홀수면 3곱해야댐
    
    else:
        if i % 2 == 0:
            res += int(arr[i])
        else: #홀수 번째
            res += 3 * int(arr[i])
            

# ans + n or ans + 3 * n 을 하고 %10 을 헸을 때 나머지 0인 수를 찾기
for i in range(10):
    if num % 2 == 0:
        # num이 짝수 -> 실제로는 홀수자리의 수 그냥 더함
        if (res + i) % 10 == 0:
            print(i)
            break
    else:
        if (res + 3 * i) % 10 == 0:
            print(i)
            break
        
