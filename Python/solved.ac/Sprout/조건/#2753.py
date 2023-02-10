inputYear = int(input())

if inputYear % 400 == 0:
    print(1)
else:
    if inputYear % 4 == 0 and inputYear % 100 != 0:
        print(1)
    else:
        print(0)