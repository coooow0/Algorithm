# 해설진은 선수들이 바로 자기 앞의 선수를 추월할 때 추월한 선수의 이름을 부름
def solution(players, callings):
    rank = {player : i for i, player in enumerate(players) }
    
    for who in callings:
        idx = rank[who] # 현재 불린 선수의 등수
        rank[who] -= 1 # 한 등수 당김 == 2등이 1등이 됨
        rank[players[idx-1]] += 1 # 원래 앞의 등수 선수는 +1 함
        players[idx], players[idx-1] = players[idx-1], players[idx]
         
    return players