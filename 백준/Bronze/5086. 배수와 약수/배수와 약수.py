def factor(a, b):
    #  약수일 때
    if b % a == 0:
        return True
    return False

def multiple(a, b):
    # 배수일 때
    if a % b == 0:
        return True
    return False
    
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if factor(a, b):
        print('factor')
    elif multiple(a, b):
        print('multiple')
    else:
        print('neither')