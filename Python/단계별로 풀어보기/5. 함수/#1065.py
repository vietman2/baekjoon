N = int(input())

def is_hansu(n):
    if n < 100:
        return True
    else:
        num = str(n)
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            return True
        else:
            return False

count = 0
for i in range(1, N+1):
    if is_hansu(i):
        count += 1
print(count)