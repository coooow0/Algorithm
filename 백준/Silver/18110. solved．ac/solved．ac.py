import math
n = int(input())
if n == 0:
    print(0)
    exit()

arr = []

for _ in range(n):
    q = int(input())
    arr.append(q)

arr.sort()

def ban(num): # 사사오입
    if num - int(num) < 0.5:
        return int(num) 
    else:
        return int(num) + 1

minus = ban(n * 0.15)
res = 0

for i in range(minus, n - minus):
    res += arr[i]

res = res / (n - (minus * 2))
print(ban(res))