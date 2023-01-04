N = int(input())

def min_packages(N):
    if N % 5 == 0:
        return N // 5
    elif N % 5 == 1:
        return N // 5 + 1
    elif N % 5 == 2:
        if N < 12:
            return -1
        else:
            return N // 5 + 2
    elif N % 5 == 3:
        return N // 5 + 1
    elif N % 5 == 4:
        if N < 9:
            return -1
        else:
            return N // 5 + 2

print(min_packages(N))