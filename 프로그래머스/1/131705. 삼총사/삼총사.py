from itertools import combinations

def solution(number):
    combo = list(combinations(number, 3))
    # 조합 3개를 뽑음
    return sum(1 for c in combo if sum(c) == 0)
    
