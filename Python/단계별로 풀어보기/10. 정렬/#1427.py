num = input()

arr = []
for i in range(len(num)):
    arr.append(int(num[i]))

arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i], end='')