import sys
input = sys.stdin.readline

def check(n):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    else:
        print(n)
    
arr = []

num, idx = 0, 0

for i in range(3):
    x = input().strip()
    arr.append(x)
    if x.isdigit():
        num = int(x)
        idx = i

if idx == 2:
    num += 1
    check(num)
elif idx == 1:
    num += 2
    check(num) 
else:
    num += 3
    check(num)