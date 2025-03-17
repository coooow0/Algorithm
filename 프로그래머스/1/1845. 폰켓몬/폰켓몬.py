def solution(nums):
    a = len(list(set(nums)))
    b = len(nums) // 2
    return min(a, b)