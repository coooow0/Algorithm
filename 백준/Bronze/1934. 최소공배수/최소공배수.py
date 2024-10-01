def lcm(a, b): #최대공약수
    if a < b:
        a, b = b, a #더 클 경우 바꿔줌
    
    while b > 0:
        c = a % b
        a, b = b, c
        
    return a

def gcd(a, b): #최소공배수
    return (a*b) // lcm(a, b)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(gcd(a, b))