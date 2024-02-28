n = int(input())
list = list(map(int, input().split()))
result = 0

for i in list:
    for j in range(2, i+1): # range(a, b)로 하면 a부터 b-1까지 하기 때문에 +1을 해주어야 함
        if i % j == 0:
            if i == j:
                result+=1
                # 소수는 1과 본인만을 약수로 가지는 수
                # i를 9라고 하고 j 를 3이라고 하면, 나머지는 0이 되지만 소수가 아니기 때문에
                # 동일 조건을 둠
            break
print(result)
