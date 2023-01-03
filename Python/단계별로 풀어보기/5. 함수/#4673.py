def selfNumber(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

list = []
for i in range(1, 10001):
    list.append(selfNumber(i))

for i in range(1, 10001):
    if i not in list:
        print(i)