def solution(new_id):

    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    arr = []
    
    for i in new_id:
        if i in ['-', '_', '.'] or ord('a') <= ord(i) and ord('z') >= ord(i) or ord('0') <= ord(i) and ord('9') >= ord(i):
            arr.append(i)
    
    new_id = arr
    
    # 3단계
    dot = 0
    arr = []
    
    for i in new_id:
        if i == '.':
            dot += 1
            
        else:
            if dot:
                arr.append('.')
                dot = 0
                arr.append(i)
            else:
                arr.append(i)
    
    # 4단계
    new_id = ''
    
    for i in arr:
        new_id += i
    new_id = new_id.strip('.')
        
    # 5단계
    
    if not len(new_id):
        new_id = 'a'
        
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
        
    
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id
