def solution(arr1, arr2):
    ans = [[] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        A = arr1[i] # [1, 2]
        B = arr2[i] # [3, 4]

        for k in range(len(A)):
            ans[i].append(A[k] + B[k])

        
    return ans