while True:
    try:
        s = list(input())
        arr = [0] * 4 # 소문자, 대문자, 숫자, 공백
        for i in range(len(s)):
            answer = ord(s[i])
            if answer == ord(' '):
                arr[3] += 1
            elif answer >= ord('a') and answer <= ord('z'):
                arr[0] += 1
            elif answer >= ord('A') and answer <= ord('Z'):
                arr[1] += 1
            elif answer >= ord('0') and answer <= ord('9'):
                arr[2] += 1
            
        for i in arr:
            print(i, end=' ')
        print()
    except:
        break
