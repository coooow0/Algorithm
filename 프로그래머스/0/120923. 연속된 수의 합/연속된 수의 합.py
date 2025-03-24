def solution(num, total):
    # 미지수 x를 둔다고 생각 ㄱ 
    mid = total // num
    # 중앙 값을 기준으로 해당 개수만큼 배치하기 위해 num - 1 // 2를 함
    start = mid - (num - 1) // 2
    
    answer = [start + i for i in range(num)]
    return answer