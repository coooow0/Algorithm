def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for num in _reserve:
        if num-1 in _lost:
            _lost.remove(num-1)
        elif num+1 in _lost:
            _lost.remove(num+1)
    
    return n-len(_lost)
