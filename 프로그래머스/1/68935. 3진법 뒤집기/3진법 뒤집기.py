def solution(n):
    ans = ''
    while True:
        if n < 3:
            return int(str(n), 3)
        if n // 3 <= 2:
            ans += str(n % 3)
            ans += str(n // 3)
            break
        
        ans += str(n % 3)
        n //= 3
    return int(ans, 3)
    
