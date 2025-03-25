def solution(id_pw, db):
    a, b = id_pw[0], id_pw[1]    
    for id, pw in db:
        if id == a and pw == b:
            return "login"
        elif id == a and pw != b:
            return "wrong pw"
    
    return "fail"