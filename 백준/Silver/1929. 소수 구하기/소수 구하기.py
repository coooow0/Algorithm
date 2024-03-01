import math
m, n = map(int, input().split())
#작은 수가 m, 큰 수가 n

for i in range(m, n+1):
    if i < 2:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        # math.sqrt는 제곱근 = 루트 씌우는 거
        if i % j == 0:
            break
    else:
        print(i)

#원래 코드
# import math
# m, n = map(int, input().split())
# #작은 수가 m, 큰 수가 n

# for i in range(m, n+1):
#     for j in range(2, int(math.sqrt(i))+1):
#         # math.sqrt는 제곱근 = 루트 씌우는 거
#         if i % j == 0:
#             break
#     print(i)

# i가 어떤 수로도 나누어 떨어지더라고 i를 출력하기에 안됨
# 어차피 i를 2부터 쓸 거 같았기에.. 상관없을줄
# i가 어떤 수로도 나누어 떨어지지 않았을 때만 i를 출력하도록 else 를 추가해야한다. 
