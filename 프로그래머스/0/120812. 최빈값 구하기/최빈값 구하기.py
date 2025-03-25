def solution(array):
    arr = list(set(array)) # 숫자를 저장함
    arr.sort()
    
    cnt = [0] * (len(arr)) # 개수를 셈
    
    for i in array:
        cnt[arr.index(i)] += 1
        
        
    many = [] # 최빈값을 담는 배열
    m = max(cnt) # 최다 개수를 구함
    
    for i in range(len(arr)):
        if cnt[i] == m:
            many.append(arr[i])
            
    if len(many) >= 2:
        return -1
    else:
        return many[0]
    
