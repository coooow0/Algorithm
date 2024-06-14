# k개를 골라 상자 하나에 담아 판매하려고 함
# 귤의 크기가 일정하지 않아 보기 좋지 않음. 귤을 크기 별로 분류했을 때 서로 다른 종류의 귤을 최소화 하고픔
# 그냥 한 크기의 갯수가 적은 귤은 안 넣고싶다. 이건듯 

def solution(k, tangerine):
    cnt = 0
    arr = dict()
    for i in tangerine:
        if i not in arr:
            arr[i] = 0
        arr[i] += 1
    
    arr = sorted(arr.items(), key=lambda x:x[1], reverse=True)
    arr = list(dict(arr).values())
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
        cnt += 1
        if k <= answer:
            break
    return cnt