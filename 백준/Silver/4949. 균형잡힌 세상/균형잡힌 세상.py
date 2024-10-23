def balance(arr):
    for k in arr:
        if len(stack) == 0 and (k == ']' or k == ')'):
            print('no')
            return False
        
        if k == '(' or k == '[':
            stack.append(k)
        elif k == ')':
            if stack[-1] != '(':
                print('no')
                return False
            else:
                stack.pop()

        elif k == ']':
            if stack[-1] != '[':
                print('no')
                return False
            else:
                stack.pop()
                        

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
            
    
while True:
    n = input()
    if n == '.':
        break
    stack = []
    n = list(n)
    balance(n)