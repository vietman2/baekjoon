A, B, V = map(int, input().split())

def get_day(A, B, V):
    if (V - B) % (A - B) == 0:
        return (V - B) // (A - B)
    else:
        return (V - B) // (A - B) + 1

print(get_day(A, B, V))