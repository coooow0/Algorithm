# 바구니 총 n개 1~n개 
# m번 바구니의 순서를 역순으로 바꿈 

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    # i번째 부터 j번째 까지 뒤집어부림
    rev = arr[i-1:j]
    rev.reverse()
    
    for x in range(len(rev)):
        arr[i - 1 + x] = rev[x]
print(*arr)