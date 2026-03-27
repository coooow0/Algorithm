# 수 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
# 메모리 제한이 8MB로 무지 적은 편. 메모리를 잘 써야한다... 
# arr[입력한 수] = 입력받은 횟수(개수)로 놓고 개수가 1개 이상이면 그만큼 출력하도록 함 
# -> 10000개의 배열을 쓸 수 있음. 아니면 10,000,000개의 배열을 써야할 수도 있음.
# 그에 반해 시간은 널널해서 for문 많이 돌려도 상관업슬듯..

arr = [0] *(10000 + 1)
for _ in range(n):
    m = int(input())
    arr[m] += 1
    
for i in range(len(arr)):
    if arr[i] != 0: # 입력받은 적이 있을 경우
        for _ in range(arr[i]):
            print(i)
    
      