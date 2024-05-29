def solution(absolutes, signs):
    for i in range(0, len(signs)):
        if signs[i] == False:
            absolutes[i] = -1 * absolutes[i]
    return sum(absolutes)