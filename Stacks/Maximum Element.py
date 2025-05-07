"""https://www.hackerrank.com/challenges/maximum-element/problem?isFullScreen=true"""

def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:
        if op[0] == '1':
            value = int(op.split()[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif op[0] == '2':
            if stack:
                removed = stack.pop()
                if removed == max_stack[-1]:
                    max_stack.pop()
        elif op[0] == '3':
            if max_stack:
                result.append(max_stack[-1])
    
    return result