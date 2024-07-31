def solution(brown, yellow):
    totalSum = brown + yellow
    for i in range(3, brown):
        if totalSum % i == 0:
            k = totalSum // i
            if (i - 2) * (k - 2) == yellow:
                return sorted([i, k], reverse=True)