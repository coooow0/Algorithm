def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        n = min(arr)
        n = arr.index(n)
        arr.pop(n)
        return arr