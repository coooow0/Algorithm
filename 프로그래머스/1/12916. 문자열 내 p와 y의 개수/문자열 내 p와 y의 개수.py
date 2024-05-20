def solution(s):
    a = s.count('p')
    a += s.count('P')
    b = s.count('y')
    b += s.count('Y')
    if a == b:
        return True 
    else:
        return False