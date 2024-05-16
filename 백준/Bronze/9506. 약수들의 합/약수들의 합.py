while True:
    n = int(input())
    if n == -1:
        break
    arr = [i for i in range(1, n) if n % i == 0]
    if n == sum(arr):
        print(n, '= ', end='')
        for i in arr:
            if i == arr[-1]:
                break
            print(i, end=' + ')
        print(arr[-1])
    else:
        print(n, 'is NOT perfect.')
        
    