X = int(input())
N = int(input())

sum = 0
for i in range(0, N):
    a, b = input().split()
    sum += int(a) * int(b)

if(sum == X):
    print('Yes')
else:
    print('No')