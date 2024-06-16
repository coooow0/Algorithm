def solution(s):
    
    cnt = 0
    for i in range(len(s)):
        if cnt == -1:
            return False
        
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
    
    if cnt == 0:
        return True
    else:
        return False