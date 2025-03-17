def gcd(a, b): # 최대공약수
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def lcm(a, b): #최소공배수
    return a * b // gcd(a, b)


def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2)
    numer1 *= denom // denom1
    numer2 *= denom // denom2
    
    numer = numer1 + numer2
    
    answer = []
    answer.append(numer // gcd(numer, denom))
    answer.append(denom // gcd(numer, denom))
    return answer