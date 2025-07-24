def back():
    if len(result) == n:
        print(*result)
        return # return이 없어도 밑에 for문 조건을 만족하지 않기 때문에 출력은 정상적으로 나옴

    
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            back()
            result.pop()
    

n = int(input())

result = []

back()