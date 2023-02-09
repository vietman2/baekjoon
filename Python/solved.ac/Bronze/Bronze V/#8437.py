N = int(input())
dif = int(input())

if(N%2 == 0):
    print((N//2)+(dif//2))
    print((N//2)-(dif//2))
else:
    print((N//2)+(dif//2)+1)
    print((N//2)-(dif//2))
