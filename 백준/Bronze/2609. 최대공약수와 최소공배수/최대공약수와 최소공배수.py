a, b = map(int, input().split())

def gcd(a, b):
    c = 1
    if a < b:
        a, b = b, a #b가 더 크면 a에 집어넣도록 함
    while b > 0:
        c = a % b
        a, b = b, c
    return a


print(gcd(a, b))
print(a*b // gcd(a,b))