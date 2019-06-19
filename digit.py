def repeatedNumber(A):
    A = sorted(A)
    index = 1
    prev = 0
    i = 0
    while(i < len(A)):
        if A[i] != index and prev != A[i]:
            missing = index
            index = A[i]
            continue
        elif A[i] == prev:
            redundant = A[i]
        else:
            index += 1
        prev = A[i]
        i = i + 1
    return [redundant, missing]

print repeatedNumber([ 2,2 ])

