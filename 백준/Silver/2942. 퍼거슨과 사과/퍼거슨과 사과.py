r, g = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = gcd(r, g)

for i in range(1, n + 1):
    if n  % i == 0:
        print(i, r // i, g // i)