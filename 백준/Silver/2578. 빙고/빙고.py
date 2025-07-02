def check():
    bg_cnt = 0
    # 1. 행을 탐색함. 0이 몇개 있는가? 0이 다섯개면 빙고. count 추가
    for i in range(5):
        if bingo[i].count(0) == 5:
            bg_cnt += 1
    
    # 2. 열을 탐색함.. 같은 열 다른 행 a[0][0], a[1][0] --- a[4][0] / a[0][1] a[1][1]
    for col in range(5):
        col_cnt = 0 # 얘가 5개가 되면 빙고임
        for row in range(5):
            if bingo[row][col] == 0:
                col_cnt += 1
            if col_cnt == 5:
                bg_cnt += 1
    
    # 3 - 1. 대각선 탐색 왼위에서 오밑
    # a[0][0] a[1][1] a[2][2] ...
    line = 0
    for i in range(5):
        if bingo[i][i] == 0:
            line += 1
            # 0의 개수를 셈
    if line == 5:
        bg_cnt += 1

    # 3 - 2. 대각선 왼밑 - 오위
    # a[4][0] a[3][1] a[2][2] a[1][3] a[0][4]
        
    line = 0
    for i in range(5):
        if bingo[4 - i][i] == 0:
            line += 1
    
    if line == 5:
        bg_cnt += 1
        
    if bg_cnt >= 3:
        print(cnt)
        exit()
    

bingo = [] #내가 적은 빙고
for _ in range(5):
    bingo.append(list(map(int,input().split())))

call = [] #사회자가 부름
for _ in range(5):
    call += list(map(int, input().split()))
    
cnt = 0
    
for i in range(25):
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == call[i]:
                bingo[j][k] = 0
                cnt += 1
            
            if cnt >=12: # 13번 이상 불려야 3빙고 가능
                check()
                