a, b = map(int, input().split())

feels = a - a*(b/100)

if(feels >= 100):
    print(0)
else:
    print(1)