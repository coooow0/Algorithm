# 그룹단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우를 말함
# 예를 들어 ccazzzzb 는 연속해서 나타남. 그룹 단어임
# aaabbcb 는 b가 떨어져서 나타나서 그룹단어가 아님

import sys
input = sys.stdin.readline

n = int(input())
answer = n
for i in range(n):
    arr = list(input().strip()) # 입력받은 문자열을 list화 함
    result = []
    for j in arr: # 각 문자의 배열을 만듦.. set을 사용하면 순서가 뒤죽박죽 되기에
        if j not in result:
            result.append(j)
    for k in range(len(arr)):
        if arr[k] != result[0]:
            if arr[k] not in result:
                answer -= 1
                break
            result.pop(0)
    
print(answer)