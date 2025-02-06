n, k = list(map(int, input().split()))
arr = [i for i in range(2, n+1)]
delete = []

while len(delete) < k:
    p = arr[0]
    remove_arr = []
    for i in arr:
        if i % p == 0:
            delete.append(i)
            remove_arr.append(i)
            
    for i in remove_arr:
        arr.remove(i)
        
print(delete[k-1])