import sys
import math
input = sys.stdin.readline

n, s = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

if n == 1:
    print(arr[0] - s)
    exit()

num = []
for i in range(n):
    num.append(abs(s - arr[i]))
    
gcd_num = math.gcd(num[0], num[1])

for i in range(2, len(num)):
    gcd_num = math.gcd(gcd_num, num[i])
print(gcd_num)