def dina(x, y, l, board):
    #x,y는 위치. l은 보드판의 길이
    x, y = x - 1, y - 1
    for row in range(x, x + 3): # 폭탄이 있는 위치의 전 위치부터 후까지
        for col in range(y, y + 3):
            if 0<= row < l and 0<= col < l:
                board[row][col] = 1
    return board

def solution(board):
    answer = 0
    boom = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                boom.append([row, col])
    
    for i in range(len(boom)):
        # 폭탄이 있는 곳 주위를 1로 만듦
        dina(boom[i][0], boom[i][1], len(board), board)
    
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                answer += 1
    return answer