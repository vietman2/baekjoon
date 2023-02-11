N = int(input())

for i in range(N):
    d, f, p = map(float, input().split())
    print("$%.2f" % (d * f * p))