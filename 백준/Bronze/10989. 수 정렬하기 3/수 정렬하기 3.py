import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * (10000+1) # 해당 수는 10000보다 작거나 같으니까

for _ in range(n):
    i = int(input())
    arr[i] += 1 # 입력받은 숫자의 배열 값이 증가함

for i in range(len(arr)):
    if arr[i] != 0: # 입력을 받은 배열이라면
        for _ in range(arr[i]): # 배열의 값 만큼 출력 
            print(i)