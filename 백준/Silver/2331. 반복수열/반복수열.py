a, p = map(int, input().split())
d = [a] # 반복 수열

def retry(n): # 숫자를 입력받음
    global idx
    arr = list(str(n)) # 한 자리씩 나눠서 배열에 집어넣음
    answer = 0
    for i in arr:
        answer += int(i) ** p
    
    if answer not in d:
        d.append(answer)    
        retry(answer)
    else: # 안에 있는 경우
        idx = d.index(answer)
        d.pop()
        return False
    
retry(a)

print(len(d[:idx]))