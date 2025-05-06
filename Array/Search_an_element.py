def search_element_in_array():
    # Input parsing
    X = map(int, input().split())
    A = list(map(int, input().split()))

    # Check if X is in A
    if X in A:
        print("YES")
    else:
        print("NO")

search_element_in_array()