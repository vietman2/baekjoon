def star(n):
    if n == 1:
        return ['*']
    else:
        n = n // 3
        a = star(n)
        b = []
        for i in range(n):
            b.append(a[i] * 3)
        for i in range(n):
            b.append(a[i] + ' ' * n + a[i])
        for i in range(n):
            b.append(a[i] * 3)
        return b

n = int(input())
for i in star(n):
    print(i)
    