# 체스판 다시 칠하기 

n, m = map(int, input().split())

chess = [''] * n
for i in range(n):
    chess[i] = input()

result = []
for i in range(n - 7):
    for j in range(m - 7):
        b_paint = 0 # 칠해야 하는 칸의 수
        w_paint = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 짝수일 경우, 시작 색과 같아야 함
                    if chess[a][b] != 'W': # 체스판에 W가 있어야 하는데, 그렇지 않기에 white를 칠해줌
                        w_paint += 1
                    if chess[a][b] != 'B': # 같아야 하는데 다른 색이 있음.. 
                        b_paint += 1
                else: # 홀수일 경우, 시작 색과 달라야 함
                    if chess[a][b] != 'W': # B로 시작해야 하는데 잘못된 경우
                        b_paint += 1
                    if chess[a][b] != 'B': # W로 시작해야 하는데 잘못된 경우 W를 칠해주어야 함.
                        w_paint += 1
        result.append(w_paint)
        result.append(b_paint)
print(min(result))