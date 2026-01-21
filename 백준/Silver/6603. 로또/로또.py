from itertools import combinations
 
while True:
    arr = list(map(int, input().strip().split()))
    
    if len(arr) == 1:
        break
    
    for i in combinations(arr[1:], 6):
        print(*i)
        
    print()