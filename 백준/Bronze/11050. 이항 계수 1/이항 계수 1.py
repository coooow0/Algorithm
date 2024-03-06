# 이항계수 = nCk = n! / (n-k)!k! = nPr / k!

n, k = map(int, input().split())
res1 = 1
for i in range(k):
    res1 = res1 * (n-i) #이 부분이 n! / (n-k)!

res2 = 1
for i in range(2, k+1):
    res2 *= i

print(res1 // res2)