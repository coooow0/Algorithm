def solution(phone_number):
    star = '*' * (len(phone_number) - 4)
    number = phone_number[-4:]
    return star + number