a, b = map(int, input().split())
# for i in range(max(a, b), a*b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
# 두 수중 큰 수로 시작을 하고, 해당 수로 두 수를 나누었을 때 나머지가 0인 경우가 최소공배수

# 최대 공약수는 둘 중 작은 수에서 시작해서 -1을 함. 두 수에서 해당 수를 나누었을 때 나머지가 0이면 최대공약수임 

def GCD(x, y):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
        
def LCM(x, y):
    return (x * y) // GCD(x, y)
print(LCM(a, b))