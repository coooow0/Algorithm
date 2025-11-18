import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()

left = 0
right = n - 1

min_sum = arr[left] + arr[right]
ans = [arr[left], arr[right]]


while right > left:
    current_sum = arr[left] + arr[right] # 현재 값
     
    if abs(current_sum) < abs(min_sum):
        min_sum = abs(current_sum)
        ans = [arr[left], arr[right]]
    
    if current_sum < 0:
        # 음수의 경우 left를 +1
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        print(arr[left], arr[right])
        exit()

print(*ans)