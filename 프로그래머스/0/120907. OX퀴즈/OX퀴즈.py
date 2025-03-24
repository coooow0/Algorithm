def solution(quiz):
    answer = []
    for str in quiz:
        arr = str.split()
        if arr[1] == '-': # 뺄셈일 경우
            if int(arr[-1]) == (int(arr[0]) - int(arr[2])):
                answer.append("O")
            else:
                answer.append("X")
        
        else: # 덧셈일 경우
            if int(arr[-1]) == (int(arr[0]) + int(arr[2])):
                answer.append("O")
            else:
                answer.append("X")
    return answer