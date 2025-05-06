

def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        q_type, x, y = query
        idx = (x ^ lastAnswer) % n
        if q_type == 1:
            seqList[idx].append(y)
        elif q_type == 2:
            lastAnswer = seqList[idx][y % len(seqList[idx])]
            result.append(lastAnswer)
    
    return result

# Example usage:
n = 2
queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]

print(dynamicArray(n, queries))
