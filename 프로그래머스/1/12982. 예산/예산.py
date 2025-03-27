def solution(d, budget):
    ans = 0
    d.sort()
    
    for i in d:
        if budget >= i: # 금액이 남았을 경우
            ans += 1
            budget -= i
        else:
            return ans  
    return ans