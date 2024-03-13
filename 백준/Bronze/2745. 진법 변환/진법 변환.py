alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
n = n[::-1] # 뒤집기
b = int(b)
result = 0
for i in range(len(n)):
    result += (b**i) * (alpha.index(n[i]))
print(result)

#리스트.index(n[i]) n[i]란 단어가 어느 위치에 있는지 알려줌 
