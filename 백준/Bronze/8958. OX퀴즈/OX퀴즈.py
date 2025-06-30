n = int(input())

for _ in range(n):
    arr = list(input())
    res = 0 # 총 점수
    before = 0 # 연속된 수인지 판별
    
    for i in range(len(arr)):
        if arr[i] == 'O': # 정답의 경우
            if before == 0: # 연속이 아닐 경우
                res += 1
                before += 1
            else: # 연속의 경우
                res += (before + 1)
                before += 1
        else:
            before = 0
    print(res)