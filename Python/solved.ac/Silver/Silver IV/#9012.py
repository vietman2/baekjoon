T = int(input())

for _ in range(T):
    stack = []
    ps = input()
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(p)
                break
    if stack:
        print('NO')
    else:
        print('YES')
