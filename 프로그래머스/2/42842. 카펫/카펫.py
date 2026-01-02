def solution(brown, yellow):
    answer = []
    
    sum = brown + yellow 
    
    for i in range(3, brown + 1):
        if sum % i == 0:
            b = sum // i
            
            if (i - 2) * (b - 2) == yellow:
                return [b, i]
