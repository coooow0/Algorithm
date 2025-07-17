import sys
input = sys.stdin.readline

def paper(r, c, l):
    # 행, 열, 길이
    color = graph[r][c] # 첫번째 종이의 색을 저장. 1이면 파란색, 0이면 흰색
    for i in range(r, r + l):
        for k in range(c, c + l):
            if graph[i][k] != color:
                # 색종이 색이 다를 경우 나누어야 함
                paper(r, c, l // 2)
                paper(r, c + l // 2, l // 2)
                paper(r + l // 2, c, l // 2)
                paper(r + l // 2, c + l // 2, l // 2)
                return # 리턴이 없으면 나눠야할 때도 밑에 if문이 돌아가서 안됨
    if color == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


n = int(input().strip())

graph = [list(map(int, input().strip().split())) for _ in range(n)]

cnt = [0, 0]

paper(0, 0, n)

print(cnt[0])
print(cnt[1])