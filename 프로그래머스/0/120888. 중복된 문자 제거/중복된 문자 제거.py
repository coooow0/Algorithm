def solution(my_string):
    my_string = list(my_string)
    arr = []
    for i in my_string:
        if i in arr:
            continue
        else:
            arr.append(i)
    answer = ''
    for i in arr:
        answer+=i
    return answer