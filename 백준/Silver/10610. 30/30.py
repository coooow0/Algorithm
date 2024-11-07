n = list(input())
n.sort(reverse=True)

ans = ''
for i in n:
    ans += i
    # 뒤집은 숫자를 문자열에 추가
    
if '0' not in ans:
    print(-1)
else:
    if int(ans) % 30 == 0:
        print(ans)
    else:
        print(-1)