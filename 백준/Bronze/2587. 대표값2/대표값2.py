arr = []

for _ in range(5):
    arr.append(int(input()))
    
print(sum(arr) // 5)
arr.sort()
print(arr[2])