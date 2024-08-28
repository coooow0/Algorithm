def solution(numlist, n):
    numlist = [i - n for i in numlist]
    numlist = sorted(numlist, key=abs)
    
    answer = []
    
    while numlist:
        if len(numlist) == 1: #하나만 남아있을 경우
            answer.append(numlist[0] + n)
            numlist.pop(0)
            
        elif abs(numlist[0]) == abs(numlist[1]): #절대값이 같을 경우
            if numlist[0] > numlist[1]: # 원래 숫자가 큰 것이 앞에 있으면 sorted를 해도 앞에 있음
                answer.append(numlist[0] + n)           
                answer.append(numlist[1] + n)
                numlist.pop(0)
                numlist.pop(0)
                
            else:
                answer.append(numlist[1] + n)
                answer.append(numlist[0] + n )
                numlist.pop(0)        
                numlist.pop(0)
            
        else: # 절대값이 같지 않을 경우
            answer.append(numlist[0] + n)
            numlist.pop(0)
            
    return answer