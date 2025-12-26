def solution(s):
    answer = s.split(' ')
    
    ans = ''
    for i in range(len(answer)):
        num = answer[i]
        
        for k in range(len(num)):
            if k % 2 == 1:
                ans += answer[i][k].lower()
            else:
                ans += answer[i][k].upper()
        if i != len(answer) - 1:
            ans += ' '
                
    return ans