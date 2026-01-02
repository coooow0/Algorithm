from itertools import permutations 
import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


def solution(numbers):
    numbers = list(numbers)
    
    cnt = 0
    arr = set()
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            num = int(''.join(list(num)))
            if is_prime(num) and num not in arr:
                arr.add(num)
                cnt += 1
    answer = 0
    return cnt