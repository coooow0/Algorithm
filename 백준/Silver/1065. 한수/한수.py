n = int(input())
cnt = 0
list_n = list(str(n))

if len(list_n) <= 2:
    for i in range(1, n+1):
        cnt += 1
else:
    cnt = 99
    for i in range(100, n+1):
        b = True # ㄷㅡㅇㅊㅏㅅㅜㅇㅕㄹ ㅇㅏㄴㅣㄴ ㄱㅓㄹ ㅊㅏㅈㅇㅡㅁ
        list_i = list(str(i))
        list_i = list(map(int, list_i)) # 100 이상의 숫자
        d = list_i[0] - list_i[1]
        for k in range(1, len(list_i)-1):
            if d != list_i[k]-list_i[k+1]:
                b = False
                break
        if b == True: # b is True, yes dungchasu
            cnt += 1
            
print(cnt)

