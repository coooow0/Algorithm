import math
n = int(input())
a = list(map(int, str(math.factorial(n))))
a.reverse()
result = 0
for i in range(len(a)):
    if a[i] == 0:
        result +=1
    else:
        break
print(result)