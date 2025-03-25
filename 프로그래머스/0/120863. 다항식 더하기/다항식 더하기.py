def solution(polynomial):
    answer = ''
    arr = list(polynomial.strip().split(" + "))
    # 항과 연산기호를 나눠줌
    x_poly = 0
    int_poly = 0
    
    for i in arr:
        if 'x' in i:
            if i == 'x':
                x_poly += 1
            else:
                x_poly += int(i[:-1])
        else:
            int_poly += int(i)
            
    if x_poly == 0:
        return str(int_poly)
    elif int_poly == 0:
        if x_poly == 1:
            return 'x'
        return str(x_poly) + 'x'
    else:
        if x_poly == 1:
            return 'x + ' + str(int_poly)
        else:
            return str(x_poly)+'x + '+str(int_poly)