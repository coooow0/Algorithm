import math
def solution(r1, r2):
    # print(math.ceil(3.1))
    # print(math.floor(3.1))
    
    answer = 0
    
    for i in range(1, r2 + 1):
    
        y_min = (r1 * r1 - i * i) # 최솟값
        if y_min < 0:
            y_min = 0
        else:
            y_min = math.ceil(math.sqrt(y_min))
        y_max = r2 * r2 - i * i
        if y_max > r2 * r2:
            y_max = r2
        else:
            y_max = math.floor(math.sqrt(y_max))
        
        
        answer += y_max - y_min + 1
    return answer * 4
        
    