def move(n, start, end):
    if n == 1:
        print(start, end)
    else:
        move(n-1, start, 6-start-end)
        print(start, end)
        move(n-1, 6-start-end, end)
n = int(input())
print(2**n-1)
move(n, 1, 3)
