n = int(input())
list = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(n):
    if list[i] == v:
        count += 1

print(count)