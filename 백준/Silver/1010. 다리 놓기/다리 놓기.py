import math
n = int(input())
result = [0 for i in range(n)]

for i in range(n):
    n, m = map(int, input().split())
    print(math.comb(m, n))
    #큰 거를 앞에 써야 함.. 