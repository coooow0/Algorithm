def solution(X, Y):
    X = list(map(int, list(str(X))))
    Y = list(map(int, list(str(Y))))
    
    answer =[]
    
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    answer.sort(reverse=True)
    string =''
    if len(set(answer)) == 1:
        return str(answer[0])
    for i in range(len(answer)):
        string+= str(answer[i])
    if string == '':
        return "-1"
    
    return string