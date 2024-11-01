n = int(input())

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, 6 - start - end) # 제일 큰 원반을 제외하고 중앙에 모음
        print(start, end) # 제일 큰 원반을 end에 놓도록 함.. 
        hanoi(n - 1, 6 - start - end, end) # 중앙에 놓은 원반을 다시 end점에 되돌림

print(2 ** n - 1)
hanoi(n, 1, 3)