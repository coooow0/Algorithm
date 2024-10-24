n = list(map(str, input().split('-')))
# 1. -를 기준으로 나눔
result = sum(list(map(int, n[0].split('+'))))
# 2. 첫번쨰 값을 무조건 더함.. +가 있을 수 있으니 그걸로 나눠서!!

if len(n) == 1:
    # 부호 값이 모두 +인 경우
    print(result)
    exit()
else:
    for i in n[1:]:
        result -= sum(list(map(int, i.split('+'))))
    print(result)