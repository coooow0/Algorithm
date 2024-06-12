def solution(before, after):
    before = list(before)
    after = list(after)
    before.sort()
    after.sort()
    if before == after:
        return 1
    else:
        return 0


