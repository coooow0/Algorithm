n = int(input())
bee = 1 #초기 벌집의 개수
cnt = 1 #몇 번 통과?
while n > bee: # 벌집의 개수가 더 많아지면 종료
    bee += 6 * cnt # 6의 배수많큼 증가
    cnt +=1
print(cnt)
