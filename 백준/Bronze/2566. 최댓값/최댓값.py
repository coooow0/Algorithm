import sys
input = sys.stdin.readline

arr = []
num = 0
mr = 0
mc = 0 # 최댓값의 인덱스를 적음

for i in range(9):
    arr.append(list(map(int, input().strip().split())))

for i in range(len(arr)):
    if max(arr[i]) > num: # 해당 배열의 제일 큰 값이 지금 있는 최대값보다 클 경우 변경
        num = max(arr[i])
        mr = i
        mc = arr[i].index(num)
    
        
        
print(num)
print(mr + 1, mc + 1)