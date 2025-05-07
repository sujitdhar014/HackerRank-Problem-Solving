def matchingStrings(strings, queries):
    result = []
    for query in queries:
        count = strings.count(query)
        result.append(count)
    return result

# Example usage:
strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']
print('\n'.join(map(str, matchingStrings(strings, queries))))




# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true