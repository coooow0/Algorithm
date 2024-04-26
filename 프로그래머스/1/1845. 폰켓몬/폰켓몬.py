def solution(nums):
    n_len = len(nums)//2 # num의 길이
    n_list = set(nums) # 중복을 없앰
    n_list = len(n_list)
    
    # 만약 중복을 없앤 값이 길이보다 길다면
    if n_list >= n_len:
        answer = n_len
    else:
        answer = n_list
    return answer