import sys
input = sys.stdin.readline
import math
n = int(input())

for i in range(n):
    n, m = map(int, input().split())
    print(math.comb(m, n))
    #큰 거를 앞에 써야 함.. 