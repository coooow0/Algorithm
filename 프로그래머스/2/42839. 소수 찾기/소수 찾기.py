from itertools import permutations
import math

def solution(numbers):
    numbers = list(numbers)
    numbers.sort(reverse=True)
    num = set()
    for i in numbers:
        num.add(int(i))
    
    big = 0
    
    # 조합이랑 큰 수 찾기
    for i in range(1, len(numbers) + 1):
        for block in permutations(numbers, i):
            block = list(block)
            block = int(''.join(block))
            num.add(block)
            big = max(block, big)
        
    answer = [True for _ in range(big+1)]
    
    for i in range(2, int(math.sqrt(big)) + 1):
        if answer[i]:
            j = 2
            while i * j <= big:
                answer[i * j] = False
                j += 1
    
    cnt = 0
    
    for i in range(2, big+1):
        if answer[i] and i in num:
            cnt +=1
        
    return cnt

