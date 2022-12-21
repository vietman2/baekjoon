N = int(input())

count = 0
value = N
while(True):
    ten = value // 10
    one = value % 10
    sum = ten + one

    new = one * 10 + sum % 10

    count+=1
    value = new

    if(new == N):
        break

print(count)