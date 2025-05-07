def arrayManipulation(n, queries):
    arr = [0] * (n + 2)  # use n+2 to avoid index issues

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max_val = 0
    current = 0
    for value in arr:
        current += value
        if current > max_val:
            max_val = current

    return max_val


# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true