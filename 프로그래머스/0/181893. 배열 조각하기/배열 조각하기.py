def solution(arr, query):
    for i in range(1, len(query) + 1):
        if i % 2 == 1: # 홀수의 경우
            arr = arr[:query[i - 1] + 1]
        else:
            arr = arr[query[i - 1]:]
    return arr