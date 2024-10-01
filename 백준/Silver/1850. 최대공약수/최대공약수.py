def gcd(a, b): #최대공약수
    if a < b:
        a, b = b, a #더 클 경우 바꿔줌
    
    while b > 0:
        c = a % b
        a, b = b, c
        
    return a

a, b = map(int, input().split())

print(gcd(a, b) *'1')