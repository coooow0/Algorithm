# 알고리즘 수업 - 점근적 표기1
# n 이상의 모든 수에서 정의되어야 함.. <- 이걸 간과함 ㅎㅠ
a, b = map(int, input().split())
c = int(input())
n = int(input())

if a > c:
    # a가 더 클 경우 n이상의 수에서 정의 xx
    # 무조건 c가 더 커야함.. 어떻게든 작아져야 하기 때문에
    print(0)
else:
    if (a - c) * n + b <= 0:
        print(1)
    else:
        print(0)