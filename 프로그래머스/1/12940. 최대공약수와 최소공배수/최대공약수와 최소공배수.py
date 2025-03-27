def solution(n, m):
    return [gcd(n, m), n * m // gcd(n ,m)]
    
def gcd(a, b): #최대 공약수
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    
    