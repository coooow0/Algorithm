n = int(input())

if n % 5 == 0:
    print(n//5) # 바로 5로 나누어지면 몫 반환
else:
    b = 0 # 3으로 나눈 값 더하기 위해서 
    while n > 0:
        n -= 3 # 값에서 3을 빼고 1을 추가해줌
        b += 1
        if n % 5 == 0: # 3을 뺀 후 5로 나누었을 때 나머지가 0이면
            b += n // 5 # b 값에 5로 나눈 몫의 값을 더해줌
            print(b)
            break
        elif n == 1 or n == 2: # 3을 뺀 값이 1 또는 2라면 나눌 수 없기 때문에 -1
            print(-1)
            break
        elif n == 0: # 3을 뺀 값이 0이면 while문을 돌은 횟수만큼 반환
            print(b)
            break
           