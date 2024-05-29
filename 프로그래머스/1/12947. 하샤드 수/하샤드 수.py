def solution(x):
    arr = list(map(int, str(x)))
    arr = sum(arr)
    if x % arr == 0:
        return True
    else:
        return False
    