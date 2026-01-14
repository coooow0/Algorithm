import math
import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().strip().split()))
# arr[0]을 기준으로.. 

for i in range(1, n):
    num = math.gcd(arr[0], arr[i])
    print(arr[0] // num, arr[i]//num, sep='/')