def solution(sizes):
    x, y = 0, 0 # 각 자리수의 최댓값을 구함
    for arr in sizes:
        arr.sort()
        x = max(arr[0], x)
        y = max(arr[1], y)
    
    return x * y