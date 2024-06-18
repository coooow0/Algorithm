s = input().upper() # 사용자에게 문자열을 입력받음
s_list = list(set(s))

cnt = []

for i in s_list: 
    count = s.count(i) # 해당 문자열의 개수를 cnt에 저장함. 이 순서는 s_list와 같다.
    cnt.append(count)
    
if cnt.count(max(cnt)) > 1: # 만약 큰 값의 개수가 1개보다 많다면. 
    print('?')
else: # 하나라면
    print(s_list[cnt.index(max(cnt))])
# 해당 맥스 값의 인덱스를 cnt에서 찾음. 그리고 그 cnt는 s_list와 순서가 같기 때문에 배열 값으로 출력한다. 