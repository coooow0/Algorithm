n, m = map(int, input().split())

pck_num = dict() # 이름을 입력받으면 번호를 출력
pck_name = dict() # 번호를 입력받으면 이름을 출력

for i in range(1, n+1):    
    name = input()
    pck_name[i] = name
    pck_num[name] = i

for _ in range(m):
    pck = input()
    if pck.isdigit():
        # 숫자 입력시
        print(pck_name[int(pck)])
    else:
        # 문자 입력시 숫자로 나타냄
        print(pck_num[pck])
    